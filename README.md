# Django_website
Learning how to make a website with Python&amp;Django.

Using blow software:    
>**Django(2.1.2    
>[django-stdimage(4.0.0](https://github.com/codingjoe/django-stdimage)    
>[django-uuslug(1.1.8](https://github.com/un33k/django-uuslug)
>[django-simple-history(2.5.1](https://github.com/treyhunner/django-simple-history/blob/master/docs/index.rst)**

What the website got now:    
>A main page ( [~/](http://sating.pythonanywhere.com/) )    
>A Gallery page ([~/gallery](http://sating.pythonanywhere.com/gallery) )

## Version 18.12.9
>*   1.Now can edit post in each post. It will check if user get permission(pk=26) or not.
>*   2.Using 'django-simple-history' app but only useable in admin.
>*   3.Fix:
>>*   3.1.photo in index.html not clickable
>>*   3.2.making comment will change post's edited_time.
## Version 18.11.27
>*   1.Fix side image that post by form(It can upload success now (Hooooray!)).
>*   2.Make the Gallery back and work great(except upload multiple upload, it still developing.)
## Version 18.11.26
>*   1.Admin filter and list.
>*   2.Add author to display in each post.
## Version 18.11.25
>*   1.Modify Post style when where is side photo or not.
>*   2.The "Stop Submit" in Post.html is keep send comment from Enter at poster input.
>*   3.Error in this version too:
>>*   3.1.Post which post by form will not contain image.
>>*   3.2.Post can't deal with the same title posts.
>>*   3.3.Login didnt set permission to do things or not(every can edit like admin)
## Version 18.11.24
>*   1.Add upload post function when login(press user name)
>*   2.Find some error:
>>*   1.Post.html post.image.url will not work when image is blank.
>>*   2.Making post will not work when upload image.
## Version 18.11.21
>*   1.Comment function susses(One little promble is that: after make comment,reload website will send message again.)
## Version 18.11.16
>*   1.Re-build whole website.
>*   2.What it got:
>*   A blog ('/')
>*   Login/Logout/Signup function
## Version 18.11.2-2
>*   1.Just simply let photo can place at the folder (YYYY/MM/DD)
## Version 18.11.2
>*   1.Upload all image and add a function to change image name by Post.slug .
>*   2.Got problem that: image upload to correct place(media/post/side/) but url will lead to wrong place(post/side/),trying to find how to solve the problem.
## Version 18.10.28
>*   1.Using 'stdimage' to get thumbnail,and link to original picture.
>*   2.Fix the problem that photo won't showout for index and Photos.
>*   3.Trying multiple files but fail.Fix will come soon ,maybe next Ver.
## Version 18.10.27
>*   1.Modify CSS of index and Post, made it simpler and refresh concepts.
>*   2.Add function to contain picture when posting.
## Version 18.10.24
>*   1.Re-edited index.html
>*   2.Add 'edited_time' for Post
>*   3.Modify time that if edited_time =/= publish_time show edited_time
>for post.html

## Version 18.10.12
>*   1.Using Flat-UI successful(^_^).
>*   2.Rebuild template/(base post index header footer).html
## Version 18.10.11
>*   1.Using Bootstraps to modify blog and post
>*   2.Trying to use [Flat-Ui](http://www.bootcss.com/p/flat-ui/) but fail(T_T)
## Version 18.10.10
>*   1.Make a app 'blog',contain some post.
>*   2.Let posts shown ny slug.
>*   3.Use "uuslug" to make unique slug for each post,
>and transfer Chinese title to pinyin slug.Learn from jianshu([Link](https://www.jianshu.com/p/2131400102a9))
## Version 18.10.6
>*   1.Make a app 'restaurants',countain some 'restaurant' 'food'    
>And 'food.name' 'food.price' .... and else.    
>*   2.Replace ( ~/menu ) to the app('restaurants') /at restaurants/views.py    
>And a table to output.    
>*   3.Add a admin to manage 'Restaurant' & 'Food'.    
