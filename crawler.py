#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import re
import urllib
import urllib2
import sys
import codecs
import string

def getPost(url):
	d = pq(url=url)
	data = d("a")
	posts_url = [] 
	for item in data.items():
		if item.attr('rel') == 'bookmark':
			posts_url.append(item.attr('href').encode('utf-8'))
	return posts_url

def getCommentsByPost(post_url):
	d = pq(url=post_url)
	data = d(".comment-content")
	comment = ''
	post_comments = []
	printable = set(string.printable)

	for item in data.items():
		comment = item('p').html().encode('utf-8')
		# filter non-ascii char
		post_comments.append(filter(lambda x: x in printable, comment))
	return ''.join(post_comments)

def getAllCommentsByBlogUrl(blog_url):
	comments = []
	posts_url = getPost(blog_url);
	for post_url in posts_url:
		post_comments = getCommentsByPost(post_url)
		comments.append(post_comments)
	return ''.join(comments)

