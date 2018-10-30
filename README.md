## Hello

Hello (future) Cyber Alchemists. First, credit where credit is due. This website was **generously**
used thanks to [Massively](#). Any modifications where subsequently made by [Caleb Ju](github.com/jucaleb4).

Now we are done, let's get to how you edit this **beast**.

First, I will discuss the structure of the files, and then how to edit it (coding/no-coding experience).

If you look at the directy, there are *a lot* of files. Don't panic, let's break it down. 
(Note: Anytime you see a "\*" it just means literally any text. It's part of [regex](https://www.rexegg.com/regex-quickstart.html)
but just not anytime I put a star, it means any file of that kind. E.g. \*.md means any file
that ends in ".md")

-> README.md (you are reading this now!)
-> index.html
-> \*.md
-> files
 |
 --> \*.\*
-> images
 |
 -> \*.png
 -> \*.jpg
-> \_posts
 |
 -> \*.md
-> \*\*

First, the `README.md` is the file you are currently reading now. Unless you made some crazy contribution, 
don't touch that.

Second, `index.html` is the home page. You likely won't need to touch that unless you know what you are doing.

Third, you will notice *a lot* of `*.md` files. These are the different pages of the website (Germ, About, etc.).
Markdown files only contain the relevant text. We keep the html files in `_include` and `_layouts`. You probably
don't want to touch those

Fourth, probably the more important one are the `/files/` and `/images/` folders. These are important,
as they hold the actual files and images we use throughout the website. If you want to add more, simply past them
into that folder (you can do it through Github by clicking the `upload new file` with the correct Github account).
Anytime you want to paste it in a markdown file, just make sure to do reference it as `/images/whatever.jpg` or
`/files/your_file.pdf`. 

Fifth, and **the** most important is the folder `_posts`. This is where any new blog post will go. Just make sure
to copy the exact format of any previous post. **Make sure** to include the (annoying) date in front of the file name
(e.g. 2018-01-01-...) otherwise the website will not pick it up.

That's it!

You can make all these changes on Github. If you can coding experience, just clone this directory to your terminal
and follow as such. Github will automatically render Jekyll files, so that makes this easy.


Credits:

	Demo Images:
		Unsplash (unsplash.com)

	Icons:
		Font Awesome (fortawesome.github.com/Font-Awesome)

	Other:
		jQuery (jquery.com)
		Misc. Sass functions (@HugoGiraudel)
		Skel (skel.io)
		Scrollex (github.com/ajlkn/jquery.scrollex)
```
