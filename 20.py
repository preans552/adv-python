class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def __str__(self):
        return f"User: {self.username}"

class Post:
    total_posts = 0

    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = 0
        self.comments = []
        Post.total_posts += 1

    def like(self):
        self.likes += 1

    def add_comment(self, comment_text, user):
        comment = Comment(comment_text, user)
        self.comments.append(comment)

    def __str__(self):
        return f"Post by {self.author.username}: {self.content} (Likes: {self.likes})"

class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def __str__(self):
        return f"{self.author.username} commented: {self.text}"

u1 = User("Alice")
u2 = User("Bob")

p1 = u1.create_post("Hello world!")
p1.like()
p1.like()
p1.add_comment("Nice post!", u2)

print(p1)
for c in p1.comments:
    print(c)

print("Total posts:", Post.total_posts)