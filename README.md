# The Finkelstein Lab

## How to Update Information

Repetitive data that changes over time (lab members, news) is stored in `_data/*.md`. If you need to add or modify a job category, those are kept in `jobtypes.md`.

Papers go in `papers/_posts/` and must have a name in the format `YYYY-MM-DD-description`. The description can be any text, but if it's absent the paper won't show up. There is a template in the `_posts` directory (template.md) that can be copied when creating a new paper from scratch. 

Other pages are typically in a directory with the same name, e.g. the "Join us!" page is in `join/join.md`. You usually should not need to modify HTML files anywhere, just the Markdown.

The links in the navigation bar at the top of each page are defined in `_includes/themes/lab/default.html`.

Homepage carousel images go in /assets/images/gallery. Member photos go in /assets/images/members.

PDFs for publications go in /assets/pdfs. Be careful when adding PDFs from a publisher that names all PDFs the same thing.   
## License

[MIT](http://opensource.org/licenses/MIT)
