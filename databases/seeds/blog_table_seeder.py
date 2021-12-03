"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Blog.create({"title":"learning to code","body":"fhfkhfkhgfkefhksehfk"})
        Blog.create({"title":"dkdkd","body":"fhfkhfkhgfkefhksehfk"})
        pass
