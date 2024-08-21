from msgspec import Struct


class Submission(Struct):

    # Required Fields
    is_self: bool
    created_utc: int | str
    selftext: str
    title: str
    score: int
    permalink: str
    over_18: bool
    num_comments: int
    id: str
    media_embed: dict
    edited: int | bool | float
    thumbnail: str

    # Optional Fields
    ups: int | None = None
    subreddit: str | None = None
    stickied: bool | None = None
    subreddit_id: str | None = None
    author: str | None = None
    secure_media: dict | None = None
    user_reports: list | None = None
    gilded: int | None = None
    secure_media_embed: dict | None = None
    downs: int | None = None
    mod_reports: list | None = None
    selftext_html: str | None = None
    retrieved_on: int | None = None
    all_awardings: list | None = None
    allow_live_comments: bool | None = None
    archived: bool | None = None
    author_created_utc: int | None = None
    author_flair_background_color: str | None = None
    author_flair_template_id: str | None = None
    author_flair_text_color: str | None = None
    awarders: list | None = None
    can_gild: bool | None = None
    can_mod_post: bool | None = None
    category: str | None = None
    content_categories: list | None = None
    contest_mode: bool | None = None
    discussion_type: str | None = None
    gildings: dict | None = None
    hidden: bool | None = None
    hide_score: bool | None = None
    is_created_from_ads_ui: bool | None = None
    is_crosspostable: bool | None = None
    is_meta: bool | None = None
    is_original_content: bool | None = None
    is_reddit_media_domain: bool | None = None
    is_robot_indexable: bool | None = None
    is_video: bool | None = None
    link_flair_background_color: str | None = None
    link_flair_richtext: list | None = None
    link_flair_template_id: str | None = None
    link_flair_text_color: str | None = None
    link_flair_type: str | None = None
    locked: bool | None = None
    media_only: bool | None = None
    name: str | None = None
    no_follow: bool | None = None
    num_crossposts: int | None = None
    parent_whitelist_status: str | None = None
    pinned: bool | None = None
    pwls: int | None = None
    quarantine: bool | None = None
    removed_by_category: str | None = None
    retrieved_utc: int | None = None
    send_replies: bool | None = None
    spoiler: bool | None = None
    subreddit_name_prefixed: str | None = None
    subreddit_subscribers: int | None = None
    subreddit_type: str | None = None
    suggested_sort: str | None = None
    thumbnail_height: int | None = None
    thumbnail_width: int | None = None
    top_awarded_type: str | None = None
    total_awards_received: int | None = None
    treatment_tags: list | None = None
    upvote_ratio: float | None = None
    url_overridden_by_dest: str | None = None
    whitelist_status: str | None = None
    wls: int | None = None
    post_hint: str | None = None
    preview: dict | None = None
    author_flair_richtext: list | None = None
    author_flair_type: str | None = None
    author_fullname: str | None = None
    author_patreon_flair: bool | None = None
    author_premium: bool | None = None
    crosspost_parent: str | None = None
    crosspost_parent_list: list | None = None
    media_metadata: dict | None = None
    brand_safe: bool | None = None
    rte_mode: str | None = None
    removal_reason: str | None = None
    saved: bool | None = None
    created: int | float | None = None
    clicked: bool | None = None
    likes: bool | None = None
    visited: bool | None = None
