## Hello

Hello (future) Cyber Alchemists. First, credit where credit is due. This website was **generously**
used thanks to [Massively](#). Any modifications where subsequently made by [Caleb Ju](github.com/jucaleb4).

Now we are done, let's get to how you edit this **beast**.

First, I will discuss the structure of the files, and then how to edit it (coding/no-coding experience).

If you look at the directy, there are *a lot* of files. Don't panic, let's break it down. 
(Note: Anytime you see a "\*" it just means literally any text. It's part of [regex](https://www.rexegg.com/regex-quickstart.html).
Simply, anytime I put a star, it means any file of that kind. E.g. \*.md means any file
that ends in ".md")

## File Structure

| First level | Second level |
|:-----------:|:-----------:|
|README.md (you are reading this now!)|
|index.html|
|\*.md|
|files|
||\*.\*
|images|
||\*.png
||\*.jpg
|\_posts|
||\*.md
|\*\*|


## Uhhh, what even are these files?
First, the `README.md` is the file you are currently reading now. Unless you made some crazy contribution, 
don't touch that.

Second, `index.html` is the home page. You likely won't need to touch that unless you know what you are doing.

Third, you will notice *a lot* of `*.md` files. These are the different pages of the website (Germ, About, etc.).
Markdown files only contain the relevant text. We keep the html files in `_include` and `_layouts`. You probably
won't need to touch these except for a few, which I will touch on later

Fourth, probably the more important one are the `/files/` and `/images/` folders. These are important,
as they hold the actual files and images we use throughout the website. If you want to add more, simply past them
into that folder (you can do it through Github by clicking the `upload new file` with the correct Github account).
Anytime you want to paste it in a markdown file, just make sure to do reference it as `/images/whatever.jpg` or
`/files/your_file.pdf`. 

Fifth, and **the** most important is the folder `_posts`. This is where any new blog post will go. Just make sure
to copy the exact format of any previous post. **Make sure** to include the (annoying) date in front of the file name
(e.g. 2018-01-01-...) otherwise the website will not pick it up.

That's it!

## What Changes to I have to Make

#### Board + Rush Start


## Making Changes
You can make all these changes on Github. If you can coding experience, just clone this directory to your terminal
and follow as such. Github will automatically render Jekyll files, so that makes this easy.

As Cyber Alchemists, you are required to update the Rush and Exec page before rush begins and place them in archives.
After the new initates, you are expected to gather and upate the Rush page with all the info. And finally, you are
expected to update the Announcements/Events page will relevant information as well as update *The Germ* will
posts and blogs and spotlights from our members on a weekly basis. 

## Why don't we use Weebly? 
I will say Weebly is easy. However, look at the quality of the website compared to other orgs 
1. [ACS](https://www.rexegg.com/regex-quickstart.html)
1. [OXE](https://illinois-oxe.weebly.com/)
1. [AIChE](http://aiche.scs.illinois.edu/) This one is pretty good actually

As you can see, this website is really good. It's also free.

Weebly with web hosting is about $140/yr. This with a Go Daddy web hosting is around $10/yr. Unless you want
to pay the extra $130 and have an average quality website, this is by far much better.


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
