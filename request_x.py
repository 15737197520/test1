import asyncio
import time

import requests
from urllib.parse import urlencode, quote  # 导入编码模块



def request_tweet(tid):
    proxies = {
        'http': 'http://127.0.0.1:10809',
        'https': 'https://127.0.0.1:10809',
    }

    url = "https://x.com/i/api/graphql/V7H0Ap3_Hh2FyS75OCDO3Q/UserTweets?" \
          "variables=%7B%22userId%22%3A%22{tid}%22%2C%22count%22%3A{count}%2" \
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
          "ePlainText%22%3A{is_plain_text}%7D".format(count="2", is_plain_text="true", tid=tid)


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
    # print(res)
    instructions = res['data']['user']['result']['timeline_v2']['timeline']['instructions']

    # 首先获取所有的推文
    entries = []
    return_data = []
    return_id_data = []
    for i in instructions:
        # if i.get("type") == 'TimelineAddEntries':
        # 处理置顶
        if "entry" in i and i.get("entry"):
            entries.append(i.get("entry"))
            print(entries)

        if "entries" in i and i.get("entries"):
            entries.extend(i.get("entries"))

    # 拿到推文的内容

    for j in entries:

        content_tmp = j.get("content").get("itemContent")
        if not content_tmp:
            continue

        legacy = content_tmp.get("tweet_results").get("result").get("legacy")
        core = content_tmp.get("tweet_results").get("result").get("core")

        if not legacy:
            continue

        operate = ""
        # 发送者
        name = core.get("user_results").get("result").get("legacy").get("name")
        entry_id = legacy.get("id_str")
        content = legacy.get("full_text")
        media = [m['media_url_https'] for m in legacy.get("entities").get("media")]

        create_time = legacy.get("created_at")
        # 转发内容
        retweeted = dict()

        if legacy.get("retweeted_status_result"):
            operate = "转发"
            # 如果是转发评论  获取真正的推文
            legacy = legacy.get("retweeted_status_result").get("result").get("legacy")
            core = legacy.get("retweeted_status_result").get("result").get("core")
            retweeted['content'] = legacy.get("full_text")
            retweeted['name'] = core.get("user_results").get("result").get("legacy").get("name")
            retweeted['media'] = [m1['media_url_https'] for m1 in legacy.get("entities").get("media")]

        print("id:\n", entry_id)
        print("content:\n", content)
        print("create_time:\n", create_time)
        print("\n-------------------------------------\n")
        return_data.append({
            "id": entry_id,
            "name": name,
            "operate": operate,
            "content": content,
            "media": media,
            "retweeted": retweeted,
            "create_time": create_time
        })
        return_id_data.append(entry_id)

    return return_data, return_id_data


# request_tweet()
