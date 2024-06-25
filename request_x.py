import requests
from urllib.parse import urlencode, quote  # 导入编码模块


proxies = {
    'http': 'http://127.0.0.1:10809',
    'https': 'https://127.0.0.1:10809',
}

url = "https://x.com/i/api/graphql/V7H0Ap3_Hh2FyS75OCDO3Q/UserTweets?" \
      "variables=%7B%22userId%22%3A%2244196397%22%2C%22count%22%3A{count}%2" \
      "C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibi" \
      "lityTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Time" \
      "line%22%3Atrue%7D&features=%7B%22rweb_tipjar_consumption_enabled%22" \
      "%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3" \
      "Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subs" \
      "criptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_gra" \
      "phql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graph" \
      "ql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22communi" \
      "ties_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_twee" \
      "t_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_ena" \
      "bled%22%3Atrue%2C%22tweetypie_unmention_optimization_enabled%22%3Atru" \
      "e%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is" \
      "_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_co" \
      "unts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumpt" \
      "ion_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consump" \
      "tion_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse" \
      "%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%2" \
      "2freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_" \
      "nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_" \
      "limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_ena" \
      "bled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atru" \
      "e%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsi" \
      "ve_web_enhance_cards_enabled%22%3Afalse%7D&fieldToggles=%7B%22withArticl" \
      "ePlainText%22%3A{is_plain_text}%7D".format(count="2", is_plain_text="true")

# 第二页url
url2 = "https://x.com/i/api/graphql/V7H0Ap3_Hh2FyS75OCDO3Q/UserTweets"

url_variables = {

        "userId": "44196397",
        "count": 2,
        "cursor": "DAABCgABGQ61Tak__-kKAAIZCawoHFqRqQgAAwAAAAIAAA",
        "includePromotedContent": True,
        "withQuickPromoteEligibilityTweetFields": True,
        "withVoice": True,
        "withV2Timeline": True,
    }

url_features = {
    "rweb_tipjar_consumption_enabled": True,
    "responsive_web_graphql_exclude_directive_enabled": True,
    "verified_phone_label_enabled": False,
    "creator_subscriptions_tweet_preview_api_enabled": True,
    "responsive_web_graphql_timeline_navigation_enabled": True,
    "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
    "communities_web_enable_tweet_community_results_fetch": True,
    "c9s_tweet_anatomy_moderator_badge_enabled": True,
    "articles_preview_enabled": True,
    "tweetypie_unmention_optimization_enabled": True,
    "responsive_web_edit_tweet_api_enabled": True,
    "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
    "view_counts_everywhere_api_enabled": True,
    "longform_notetweets_consumption_enabled": True,
    "responsive_web_twitter_article_tweet_consumption_enabled": True,
    "tweet_awards_web_tipping_enabled": False,
    "creator_subscriptions_quote_tweet_preview_enabled": False,
    "freedom_of_speech_not_reach_fetch_enabled": True,
    "standardized_nudges_misinfo": True,
    "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
    "rweb_video_timestamps_enabled": True,
    "longform_notetweets_rich_text_read_enabled": True,
    "longform_notetweets_inline_media_enabled": True,
    "responsive_web_enhance_cards_enabled": False
}
# TODO True和False有什么区别
fieldToggles = {"withArticlePlainText": False}

print(urlencode(url_features))

# url2_with_encoder = quote(url_keyword_dict, safe=True)

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 "
        "(KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",

    "X-Csrf-Token": "4e006e703ba030e8c5ade91b0c4c5e44319315fb07da1cace825abbd5197ce5a253d2bc1bbe903f7a0ed61fb54eff83a994d7320d5ea20e6affb43638bb5fb123186ee9401b0cb722a7d81a2cc27bddb",

    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Z"
                     "v7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "Cookie": "guest_id=v1%3A171879693955876715; "
        "night_mode=2; "
        "guest_id_marketing=v1%3A171879693955876715; "
        "guest_id_ads=v1%3A171879693955876715; "
        "kdt=CJjl0xg0bb2mOfQBElq8aUrrSOKcS3O3nDUg6WLG; "
        "lang=en; dnt=1; "
        "_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCFPyWzCQAToMY3NyZl9p%250AZCIlYzYwNmUzNjgzN2RjMTQ0NGNkZDFhMmYwZDVjMGNlZTU6B2lkIiU5YWRh%250AYzU2ZGY5Y2ZkMGNkYWQzYWRlMTIwYmQzNGFiMQ%253D%253D--cf2b850e62adfd4c73c88f691de863b085904760; "
        "personalization_id=v1_2Jd2Z15MhYaJ9/xZ8RNp4Q==; "
        "g_state={i_l:0}; "
        "auth_token=155f37104116db0bdcfe8b47722670bf29518cda; "
        "ct0=4e006e703ba030e8c5ade91b0c4c5e44319315fb07da1cace825abbd5197ce5a253d2bc1bbe903f7a0ed61fb54eff83a994d7320d5ea20e6affb43638bb5fb123186ee9401b0cb722a7d81a2cc27bddb; "
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     "twid=u%3D1803391245861134336"
}

res = requests.get(url=url, headers=headers, proxies=proxies).json()
print(res.url)
print(res)
instructions = res['data']['user']['result']['timeline_v2']['timeline']['instructions']
the_list = instructions['']
