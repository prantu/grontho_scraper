# -*- coding: utf-8 -*-

import re


class FeatureExtractor(object):

    OS_REGEX = re.compile('.*(\d+\.?\d+?).*')

    PROCESSOR_RANKS = {
        'single': 1,
        'dual': 2,
        'quad': 4,
        'hexa': 6,
        'octa': 8
    }

    def __extract_price__(self, string_):
        segments = string_.split()

        for segment in segments:
            if segment[0].isdigit():
                return float(segment.replace(',', ''))

    def __rank_core__(self, string_):
        score = 0

        for gimmick in self.PROCESSOR_RANKS.keys():
            if gimmick in string_.lower():
                score += self.PROCESSOR_RANKS.get(gimmick)

        return score if score > 0 else 1

    def __extract_from_str__(self, feature_string, keywords, filter_=True):
        feature_string = feature_string.lower().split()
        keywords = [keyword.lower() for keyword in keywords]

        retval = None

        for keyword in keywords:
            for segment in feature_string:
                if keyword in segment:
                    if keyword == segment:
                        retval = feature_string[feature_string.index(segment) - 1]
                        break
                    val = segment[:segment.index(keyword)]
                    if val:
                        retval = val
                        break
        if retval is not None:
            retval = float(retval)
            return retval / 1024 if filter_ and retval >= 128 else retval

    def __score_os__(self, os_string):
        os_string = os_string.lower()

        scores = {
            'marshmallow': 6.0,
            'lolipop': 5.0,
            'kitkat': 4.4,
            'kit kat': 4.4
        }

        match = self.OS_REGEX.match(os_string)
        if match and match.groups()[0] is not None:
            return float(match.groups()[0])
        else:
            for version in scores.keys():
                if version in os_string:
                    return scores.get(version)

        return 0.0

    def process_item(self, item, spider):
        item['os'] = self.__score_os__(item['os'])
        item['battery'] = self.__extract_from_str__(item['battery'], ['mAh'],
                                                    filter_=False)
        item['ram'] = self.__extract_from_str__(item['ram'], ['GB', 'MB'])
        item['rom'] = self.__extract_from_str__(item['rom'], ['GB', 'MB'])
        item['processor_core'] = self.__rank_core__(item['processor'])
        item['processor'] = self.__extract_from_str__(item['processor'],
                                                      ['GHz'])
        item['display'] = self.__extract_from_str__(item['display'], ['"'])
        item['price'] = self.__extract_price__(item['price'])
        return item
