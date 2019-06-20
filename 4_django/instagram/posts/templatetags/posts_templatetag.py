from django import template

register = template.Library()

@register.filter
def hashtag_link(post):
    #   #멀캠
    #   <a>#멀캠</a>
    content = post.content
    #   [H obj (1), H obj (3), H obj (6)]
    hashtags = post.hashtags.all()

    for hashtag in hashtags:
        content = content.replace(
            f'{hashtag.content}',                   # 가져오는 모양
            f'<a href="/posts/hashtags/{hashtag.id}">{hashtag.content}</a>'  # 바꿀 모양
        )

    return content