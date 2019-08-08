a = [
  {
    "name": "created_at",
    "type": "TIMESTAMP",
    "mode": "NULLABLE"
  },
  {
    "name": "id",
    "type": "INTEGER",
    "mode": "NULLABLE"
  },
  {
    "name": "id_str",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "extended_entities",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "media",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "source_status_id_str",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "expanded_url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "display_url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "media_url_https",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "source_status_id",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "id_str",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "sizes",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "small",
                "type": "RECORD",
                "mode": "NULLABLE",
                "fields": [
                  {
                    "name": "h",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "resize",
                    "type": "STRING",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "w",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  }
                ]
              },
              {
                "name": "large",
                "type": "RECORD",
                "mode": "NULLABLE",
                "fields": [
                  {
                    "name": "h",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "resize",
                    "type": "STRING",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "w",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  }
                ]
              },
              {
                "name": "medium",
                "type": "RECORD",
                "mode": "NULLABLE",
                "fields": [
                  {
                    "name": "h",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "resize",
                    "type": "STRING",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "w",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  }
                ]
              },
              {
                "name": "thumb",
                "type": "RECORD",
                "mode": "NULLABLE",
                "fields": [
                  {
                    "name": "h",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "resize",
                    "type": "STRING",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "w",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  }
                ]
              }
            ]
          },
          {
            "name": "indices",
            "type": "INTEGER",
            "mode": "REPEATED"
          },
          {
            "name": "type",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "id",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "media_url",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      }
    ]
  },
  {
    "name": "text",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "source",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "truncated",
    "type": "BOOLEAN",
    "mode": "NULLABLE"
  },
  {
    "name": "in_reply_to_status_id",
    "type": "INTEGER",
    "mode": "NULLABLE"
  },
  {
    "name": "in_reply_to_status_id_str",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "in_reply_to_user_id",
    "type": "INTEGER",
    "mode": "NULLABLE"
  },
  {
    "name": "in_reply_to_user_id_str",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "in_reply_to_screen_name",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "user",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "id",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "id_str",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "name",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "screen_name",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "location",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "url",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "description",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "protected",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "verified",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "followers_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "friends_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "listed_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "favourites_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "statuses_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
      },
      {
        "name": "utc_offset",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "time_zone",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "geo_enabled",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "lang",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "contributors_enabled",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "is_translator",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "translator_type",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_background_color",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_background_image_url",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_background_image_url_https",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_background_tile",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_link_color",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_sidebar_border_color",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_sidebar_fill_color",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_text_color",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_use_background_image",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_image_url",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_image_url_https",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "profile_banner_url",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "default_profile",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "default_profile_image",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "following",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "follow_request_sent",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "notifications",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "name": "geo",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "type",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "coordinates",
        "type": "FLOAT",
        "mode": "REPEATED"
      }
    ]
  },
  {
    "name": "coordinates",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "type",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "coordinates",
        "type": "FLOAT",
        "mode": "REPEATED"
      }
    ]
  },
{
    "name": "place",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "id",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "url",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "place_type",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "name",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "full_name",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "country_code",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "country",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "bounding_box",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "type",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "coordinates",
            "type": "FLOAT",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "attributes",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "name": "contributors",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "retweeted_status",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
      },
      {
        "name": "scopes",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "followers",
            "type": "BOOLEAN",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "id",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "extended_entities",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "media",
            "type": "RECORD",
            "mode": "REPEATED",
            "fields": [
              {
                "name": "expanded_url",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "source_status_id_str",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "source_status_id",
                "type": "INTEGER",
                "mode": "NULLABLE"
              },
              {
                "name": "display_url",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "url",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "media_url_https",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "id_str",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "sizes",
                "type": "RECORD",
                "mode": "NULLABLE",
                "fields": [
                  {
                    "name": "large",
                    "type": "RECORD",
                    "mode": "NULLABLE",
                    "fields": [
                      {
                        "name": "h",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "resize",
                        "type": "STRING",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "w",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      }
                    ]
                  },
                  {
                    "name": "small",
                    "type": "RECORD",
                    "mode": "NULLABLE",
                    "fields": [
                      {
                        "name": "h",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "resize",
                        "type": "STRING",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "w",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      }
                    ]
                  },
                  {
                    "name": "medium",
                    "type": "RECORD",
                    "mode": "NULLABLE",
                    "fields": [
                      {
                        "name": "h",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "resize",
                        "type": "STRING",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "w",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      }
                    ]
                  },
                  {
                    "name": "thumb",
                    "type": "RECORD",
                    "mode": "NULLABLE",
                    "fields": [
                      {
                        "name": "h",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "resize",
                        "type": "STRING",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "w",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      }
                    ]
                  }
                ]
              },
              {
                "name": "indices",
                "type": "INTEGER",
                "mode": "REPEATED"
              },
              {
                "name": "type",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "id",
                "type": "INTEGER",
                "mode": "NULLABLE"
              },
              {
                "name": "media_url",
                "type": "STRING",
                "mode": "NULLABLE"
              }
            ]
          }
        ]
      },
      {
        "name": "id_str",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "text",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "source",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "truncated",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "in_reply_to_status_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "in_reply_to_status_id_str",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "in_reply_to_user_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "in_reply_to_user_id_str",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "in_reply_to_screen_name",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "reply_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "quote_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "user",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "id",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "id_str",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "name",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "screen_name",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "location",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "description",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "protected",
            "type": "BOOLEAN",
            "mode": "NULLABLE"
          },
          {
            "name": "verified",
            "type": "BOOLEAN",
            "mode": "NULLABLE"
          },
          {
            "name": "followers_count",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "friends_count",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "listed_count",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "favourites_count",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "statuses_count",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "created_at",
            "type": "TIMESTAMP",
            "mode": "NULLABLE"
          },
          {
            "name": "utc_offset",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "time_zone",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "geo_enabled",
            "type": "BOOLEAN",
            "mode": "NULLABLE"
          },
          {
            "name": "lang",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "contributors_enabled",
            "type": "BOOLEAN",
            "mode": "NULLABLE"
          },
          {
            "name": "is_translator",
            "type": "BOOLEAN",
            "mode": "NULLABLE"
          },
          {
            "name": "translator_type",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_background_color",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_background_image_url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_background_image_url_https",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_background_tile",
            "type": "BOOLEAN",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_link_color",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_sidebar_border_color",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_sidebar_fill_color",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_text_color",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_use_background_image",
            "type": "BOOLEAN",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_image_url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_image_url_https",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "profile_banner_url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "default_profile",
            "type": "BOOLEAN",
            "mode": "NULLABLE"
          },
          {
            "name": "default_profile_image",
            "type": "BOOLEAN",
            "mode": "NULLABLE"
          },
          {
            "name": "following",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "follow_request_sent",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "notifications",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "geo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "type",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "pl",
            "type": "FLOAT",
            "mode": "REPEATED"
          },
          {
            "name": "coordinates",
            "type": "FLOAT",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "coordinates",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "type",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "coordinates",
            "type": "FLOAT",
            "mode": "REPEATED"
          }
        ]
      },
{
    "name": "place",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "id",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "url",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "place_type",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "name",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "full_name",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "country_code",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "country",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "bounding_box",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "type",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "coordinates",
            "type": "FLOAT",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "attributes",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
      {
        "name": "contributors",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "retweet_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "favorite_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "entities",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "hashtags",
            "type": "RECORD",
            "mode": "REPEATED",
            "fields": [
              {
                "name": "text",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "indices",
                "type": "INTEGER",
                "mode": "REPEATED"
              }
            ]
          },
          {
            "name": "trends",
            "type": "STRING",
            "mode": "REPEATED",
            "fields": [

            ]
          },
          {
            "name": "urls",
            "type": "RECORD",
            "mode": "REPEATED",
            "fields": [
              {
                "name": "url",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "expanded_url",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "display_url",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "indices",
                "type": "INTEGER",
                "mode": "REPEATED"
              }
            ]
          },
          {
            "name": "user_mentions",
            "type": "RECORD",
            "mode": "REPEATED",
            "fields": [
              {
                "name": "screen_name",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "name",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "id",
                "type": "INTEGER",
                "mode": "NULLABLE"
              },
              {
                "name": "id_str",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "indices",
                "type": "INTEGER",
                "mode": "REPEATED"
              }
            ]
          },
          {
            "name": "symbols",
            "type": "RECORD",
            "mode": "REPEATED",
            "fields": [
              {
                "name": "indices",
                "type": "INTEGER",
                "mode": "REPEATED"
              },
              {
                "name": "text",
                "type": "STRING",
                "mode": "NULLABLE"
              }
            ]
          },
          {
            "name": "media",
            "type": "RECORD",
            "mode": "REPEATED",
            "fields": [
              {
                "name": "id",
                "type": "INTEGER",
                "mode": "NULLABLE"
              },
              {
                "name": "id_str",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "indices",
                "type": "INTEGER",
                "mode": "REPEATED"
              },
              {
                "name": "media_url",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "media_url_https",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "url",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "display_url",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "expanded_url",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "type",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "source_status_id",
                "type": "INTEGER",
                "mode": "NULLABLE"
              },
              {
                "name": "source_status_id_str",
                "type": "STRING",
                "mode": "NULLABLE"
              },
              {
                "name": "sizes",
                "type": "RECORD",
                "mode": "NULLABLE",
                "fields": [
                  {
                    "name": "large",
                    "type": "RECORD",
                    "mode": "NULLABLE",
                    "fields": [
                      {
                        "name": "w",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "h",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "resize",
                        "type": "STRING",
                        "mode": "NULLABLE"
                      }
                    ]
                  },
                  {
                    "name": "medium",
                    "type": "RECORD",
                    "mode": "NULLABLE",
                    "fields": [
                      {
                        "name": "w",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "h",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "resize",
                        "type": "STRING",
                        "mode": "NULLABLE"
                      }
                    ]
                  },
                  {
                    "name": "thumb",
                    "type": "RECORD",
                    "mode": "NULLABLE",
                    "fields": [
                      {
                        "name": "w",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "h",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "resize",
                        "type": "STRING",
                        "mode": "NULLABLE"
                      }
                    ]
                  },
                  {
                    "name": "small",
                    "type": "RECORD",
                    "mode": "NULLABLE",
                    "fields": [
                      {
                        "name": "w",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "h",
                        "type": "INTEGER",
                        "mode": "NULLABLE"
                      },
                      {
                        "name": "resize",
                        "type": "STRING",
                        "mode": "NULLABLE"
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "name": "favorited",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "retweeted",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "timestamp_ms",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "possibly_sensitive",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "filter_level",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "lang",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "name": "retweet_count",
    "type": "INTEGER",
    "mode": "NULLABLE"
  },
  {
    "name": "favorite_count",
    "type": "INTEGER",
    "mode": "NULLABLE"
  },
  {
    "name": "entities",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "hashtags",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "text",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "indices",
            "type": "INTEGER",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "trends",
        "type": "STRING",
        "mode": "REPEATED",
        "fields": [

        ]
      },
      {
        "name": "urls",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "expanded_url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "display_url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "indices",
            "type": "INTEGER",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "user_mentions",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "screen_name",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "name",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "id",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "id_str",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "indices",
            "type": "INTEGER",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "symbols",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "indices",
            "type": "INTEGER",
            "mode": "REPEATED"
          },
          {
            "name": "text",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "media",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "id",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "id_str",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "indices",
            "type": "INTEGER",
            "mode": "REPEATED"
          },
          {
            "name": "media_url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "media_url_https",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "display_url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "expanded_url",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "type",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "sizes",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "large",
                "type": "RECORD",
                "mode": "NULLABLE",
                "fields": [
                  {
                    "name": "w",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "h",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "resize",
                    "type": "STRING",
                    "mode": "NULLABLE"
                  }
                ]
              },
              {
                "name": "medium",
                "type": "RECORD",
                "mode": "NULLABLE",
                "fields": [
                  {
                    "name": "w",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "h",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "resize",
                    "type": "STRING",
                    "mode": "NULLABLE"
                  }
                ]
              },
              {
                "name": "thumb",
                "type": "RECORD",
                "mode": "NULLABLE",
                "fields": [
                  {
                    "name": "w",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "h",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "resize",
                    "type": "STRING",
                    "mode": "NULLABLE"
                  }
                ]
              },
              {
                "name": "small",
                "type": "RECORD",
                "mode": "NULLABLE",
                "fields": [
                  {
                    "name": "w",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "h",
                    "type": "INTEGER",
                    "mode": "NULLABLE"
                  },
                  {
                    "name": "resize",
                    "type": "STRING",
                    "mode": "NULLABLE"
                  }
                ]
              }
            ]
          },
          {
            "name": "source_status_id",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "source_status_id_str",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      }
    ]
  },
  {
    "name": "favorited",
    "type": "BOOLEAN",
    "mode": "NULLABLE"
  },
  {
    "name": "retweeted",
    "type": "BOOLEAN",
    "mode": "NULLABLE"
  },
  {
    "name": "timestamp_ms",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "possibly_sensitive",
    "type": "BOOLEAN",
    "mode": "NULLABLE"
  },
  {
    "name": "filter_level",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "lang",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {"name":"el_error", 
   "type": "STRING"
  },
  {
    "name": "countryName",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "latitude_geonames",
    "type": "FLOAT",
    "mode": "NULLABLE"
  },
  {
    "name": "longitude_geonames",
    "type": "FLOAT",
    "mode": "NULLABLE"
  }
]

import apache_beam as beam
import json 
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io.gcp.pubsub import ReadFromPubSub
from cStringIO import StringIO
import logging
import traceback
import collections
import datetime
import time
import requests
from apiclient import discovery
from dateutil import parser
import httplib2
from oauth2client.client import GoogleCredentials

def coordenadas_geonames(text):
      """Uses GeoNames parser to return the coordinates from a given text"""
      url = 'https://ws.geonames.net/searchJSON'
      params = {'username':'guticamilo','fuzzy': '0.8', 'q':text}
      
      if text==None:
        return None
      else:
        r = requests.get(url, params=params)
        if r.json()['totalResultsCount']==0: 
           return None
        else:
#            try:
            if 'geonames' in r.json().keys():
                json_c=r.json()['geonames'][0]
                the_list = [json_c["countryName"], json_c["lat"], json_c["lng"]]
                return the_list
#            except KeyError:
            else:
                return None
            
def compute_points(tweet):
  """Compute points based on the record containing the match result.
  The function assigns 3 points for a win, 1 point for a draw, and 0 points for
  a loss (see http://en.wikipedia.org/wiki/Three_points_for_a_win).
  """
  try:
        location = tweet['user']['location']
        list_loc = coordenadas_geonames(location)
        tweet["countryName"] = list_loc[0]
        tweet["latitude_geonames"] =  float(list_loc[1])
        tweet["longitude_geonames"] =  float(list_loc[2])
        return tweet
#  except KeyError:
  except Exception, e:
        error= str(traceback.format_exc())
        tweet["el_error"]= "COMPUTE POINTS: " + error
#        tweet["countryName"], tweet["latitude_geonames"],tweet["longitude_geonames"] = None, None, None
        return tweet

def flatten(lst):
    """Helper function used to massage the raw tweet data."""
    for el in lst:
        if (isinstance(el, collections.Iterable) and
                not isinstance(el, basestring)):
            for sub in flatten(el):
                yield sub
        else:
            yield el

def cleanup(data):
    """Do some data massaging."""
    if isinstance(data, dict):
        newdict = {}
        for k, v in data.items():
            if (k == 'coordinates') and isinstance(v, list):
                # flatten list
                newdict[k] = list(flatten(v))
            elif k == 'created_at' and v:
                newdict[k] = str(parser.parse(v))
            # temporarily, ignore some fields not supported by the
            # current BQ schema.
            # TODO: update BigQuery schema
            elif (k == 'video_info' or k == 'scopes' or k == 'withheld_in_countries'
                  or k == 'is_quote_status' or 'source_user_id' in k
                  or k == ''
                  or 'quoted_status' in k or 'display_text_range' in k or 'extended_tweet' in k
                  or 'media' in k):
                pass
            elif v is False:
                newdict[k] = v
            else:
                if k and v:
                    newdict[k] = cleanup(v)
        return newdict
    elif isinstance(data, list):
        newlist = []
        for item in data:
            newdata = cleanup(item)
            if newdata:
                newlist.append(newdata)
        return newlist
    else:
        return data

def JsonCoder(test):
#   from cStringIO import StringIO
   body=test 
#   logging.warning(body) 
#   logging.warning(type(body))
   try:
     b = json.loads(body)
     mtweet=cleanup(b)
     if not (('delete' in mtweet) or ('limit' in mtweet)):
        yield mtweet
   except Exception, e:
     error= str(traceback.format_exc())
     yield {"el_error":error }
        
#   except:
#     b= "NO CONVIRTIO " + body 
#   logging.warning("tipo", str(type(b)))
#   logging.warning("b", str(b)) 
#   return {"todo":str(b), "tipo":str(type(b)) }


table_schema = {'fields': a}

options = PipelineOptions()
options.view_as(StandardOptions).streaming = True
options.view_as(StandardOptions).runner = 'DataflowRunner'
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'servinf-geomark-social-prod'
google_cloud_options.job_name = 'tweet-3v4'
google_cloud_options.staging_location = 'gs://temp-dataflow-t/binaries'
google_cloud_options.temp_location = 'gs://temp-dataflow-t/temp'
options.view_as(SetupOptions).save_main_session = True

with beam.Pipeline(options=options) as p:
    from apache_beam.io.gcp.internal.clients import bigquery
#    p = beam.Pipeline(options=options)
#   input = 'gs://{0}/javahelp/*.java'.format(BUCKET)
#   output_prefix = 'gs://{0}/javahelp/output'.format(BUCKET)
#   searchTerm = 'import'

   # find all lines that contain the searchTerm
    
    (p
      | 'Get_Pubsub' >> ReadFromPubSub(topic="projects/servinf-geomark-social-prod/topics/tweets")  #, with_attributes=True)
      | 'read' >> beam.FlatMap(JsonCoder)
      | 'Geonames' >> beam.Map(compute_points)
      | 'write' >> beam.io.WriteToBigQuery(
        'servinf-geomark-social-prod:Twittero.example_v4',  schema=table_schema,
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
      )
    )
p.run()

