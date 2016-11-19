#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.customer.shared.footer import footer_data_provider
from flask_app.data_providers.customer.shared.header import header_data_provider

from flask import url_for


class BlogPostDataProvider:
    # blog_page_to_return can be None
    def __init__(self):
        pass

    def get_data(self, blog_post_id, blog_page_to_return):
        return self.sample_data_0(blog_page_to_return)

    def get_page_heading_data(self, post_title, blog_url_to_return):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Blog",
                    "href": blog_url_to_return,
                },
                {
                    "name": post_title,
                },
            ],
            "title": post_title,
            "blog_post_date": "17/10/2016",
        }

    def sample_data_0(self, blog_page_to_return):
        post_title = "Vc acabou de ler o que seria o título do post =)"
        blog_url_to_return = url_for("blog", page=blog_page_to_return)
        data = {
            "header_data": header_data_provider.get_data(),
            "page_heading_data": self.get_page_heading_data(post_title=post_title,
                                                            blog_url_to_return=blog_url_to_return),
            "footer_data": footer_data_provider.get_data(),
            "title": post_title,
            "blog_url_to_return": blog_url_to_return,
            "content": """
                <p>Fusce ac pharetra urna. Duis non lacus sit amet lacus interdum facilisis sed non est. Ut mi metus, semper eu dictum nec, condimentum sed sapien. Nullam lobortis nunc semper ipsum luctus ut viverra ante eleifend. Nunc pretium velit sed augue luctus accumsan.</p>
                <div class="image-container" style="width: 600px;">
                    <img src="/static/images/blog-img1.jpg">
                </div>
                <p>Aliquam laoreet consequat malesuada. Integer vitae diam sed dolor euismod laoreet eget ac felis. Donec non erat sed elit bibendum sodales. Donec eu cursus velit. Proin nunc lacus, gravida mollis dictum ut, vulputate eu turpis. Sed felis sapien, commodo in iaculis in, feugiat sed enim. Sed nunc ipsum, fermentum varius dignissim vitae, blandit et ante.Maecenas sagittis, lorem sed congue egestas, lectus purus congue nisl, ac molestie enim ligula nec eros. Sed leo tortor, tincidunt sit amet elementum vel, eleifend at orci. Maecenas ut turpis felis. Donec sit amet quam sem, et aliquet est.</p>
                <p>Quisque nisl lectus, accumsan et euismod eu, sollicitudin ac augue. In sit amet urna magna. Curabitur imperdiet urna nec purus egestas eget aliquet purus iaculis. Nunc porttitor blandit imperdiet. Nulla facilisi. Cras odio ipsum, vehicula nec vehicula sed, convallis scelerisque quam. Phasellus ut odio dui, ut fermentum neque.</p>
                <blockquote>Lorem ipsum dolor sit amet, consecte adipiscing elit. Integer aliquam mi nec dolor placerat a condimentum diam mollis. Ut pulvinar neque eget massa dapibus dolor.</blockquote>
                <div class="image-container" style="width: 600px;">
                    <img src="/static/images/blog-img1.jpg">
                </div>
                <p>Curabitur at vestibulum sem. Aliquam vehicula neque ac nibh suscipit ultrices. Morbi interdum accumsan arcu nec scelerisque. Phasellus eget purus nulla. Suspendisse quam est, tempor quis consectetur non, interdum vitae diam. Pellentesque volutpat mollis ligula in laoreet. Aenean est dui, sagittis in consequat at, adipiscing at risus. Sed suscipit, est vitae aliquam molestie, sem dolor dignissim leo, eget imperdiet enim urna in justo. Mauris pulvinar tortor lorem. Aliquam sed nisl in ipsum tincidunt ultrices.</p>
                <h2>Heading</h2>
                Pellentesque volutpat mollis ligula in laoreet. Aenean est dui, sagittis in consequat at, adipiscing at risus. Sed suscipit, est vitae aliquam molestie, sem dolor dignissim leo, eget imperdiet enim urna in justo. Mauris pulvinar tortor lorem. Aliquam sed nisl in ipsum tincidunt ultrices.
                <ul>
                    <li> Integer vitae diam sed dolor euismod laoreet eget ac felis</li>
                    <li> Integer vitae diam sed dolor euismod laoreet eget ac felis</li>
                    <li> Integer vitae diam sed dolor euismod laoreet eget ac felis</li>
                    <li> Integer vitae diam sed dolor euismod laoreet eget ac felis</li>
                    <li> Integer vitae diam sed dolor euismod laoreet eget ac felis</li>
                </ul>
                <h3>Heading</h3>
                <div class="video-container">
                    <iframe width="700px" src="https://www.youtube.com/embed/XGSy3_Czz8k"></iframe>
                </div>
                Pellentesque volutpat mollis ligula in laoreet. Aenean est dui, sagittis in consequat at, adipiscing at risus. Sed suscipit, est vitae aliquam molestie, sem dolor dignissim leo, eget imperdiet enim urna in justo. Mauris pulvinar tortor lorem. Aliquam sed nisl in ipsum tincidunt ultrices.
                <h4>Heading</h4>
                <p>Nullam commodo lobortis nibh, vitae accumsan velit dapibus sed. Nunc ac sem eu libero pretium faucib. Quisque et semper odio. Praesent tortor ligula, imperdiet sed aliquet ut, pharetra at nisi. Etiam sit amet molestie est. Donec id turpis vitae leo viverra adipiscing at sed nisi. Donec ut justo nunc. Vivamu bibendum erat ac nunc sollicitudin lacinia. Phasellus sed lacus magna.</p>
                <h5>Heading</h5>
                <p>Nullam commodo lobortis nibh, vitae accumsan velit dapibus sed. Nunc ac sem eu libero pretium faucib. Quisque et semper odio. Praesent tortor ligula, imperdiet sed aliquet ut, pharetra at nisi. Etiam sit amet molestie est. Donec id turpis vitae leo viverra adipiscing at sed nisi. Donec ut justo nunc. Vivamu bibendum erat ac nunc sollicitudin lacinia. Phasellus sed lacus magna.</p>
            """,
        }
        return data

blog_post_data_provider = BlogPostDataProvider()
