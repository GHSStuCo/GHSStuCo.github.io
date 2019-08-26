# ghsstucowebsite
Grinnell High School's Student Council Website.

## Making Changes
After you have made a change, from the root directory, run `make`. Then, you'll want to add, commit, and push the changes to the git repository to have your changes show up on the website (e.g., `git add * && git commit -m "Updated file" && git push`).

### Changing Committee Information
Change `text/Documents.txt`. The format of the document is as follows:
```
*COMMITTEE 1 NAME|(COMMITTEE 1 CHAIR NAME - Chair)
COMMITTEE MEMBER #1
COMMITTEE MEMBER #2
...
COMMITTEE MEMBER #3

*COMMITTEE 2 NAME|(COMMITTEE 2 CHAIR NAME - Chair)
COMMITTEE MEMBER #1
COMMITTEE MEMBER #2
...
COMMITTEE MEMBER #3

etc...
```
For example,
```
*Website Committee|(John Smith - Chair)
John Smith
Mary Smith
Sam Smith
Sal Smith

*Random Committee|(Jane Doe - Chair)
Jane Doe
Mary Doe
Sam Doe
John Doe
```


### Changing Members List
Change `text/Members.txt`. The format of the document is as follows:
```
##GroupName	groupnameid
Image_File_Name		Position	Name	Bio
Image_File_Name		Position	Name	Bio
Image_File_Name		Position	Name	Bio

##GroupName	groupnameid
Image_File_Name		Position	Name	Bio
Image_File_Name		Position	Name	Bio
Image_File_Name		Position	Name	Bio
```
(Note that the tabs are important.)
For example,
```
##Executive Members	executive
John	Student Body President	John Smith	John Smith is an outgoing individual.
Jane	Student Body Vice President	Jane Doe	Jane Doe is also an outgoing individual.

##Senior Class	senior
Bob	Senior Class President	Bob Doe	Bob Doe is brother to Jane.
Sal	Senior Class Representative	Sal Smith	Sal Smith is sister to John.
```

## Adding a page
To create a page named `name` you will want to do the following:

### 1. Add the file to the header.

Open up `html/base.html` and add another `<li>` element of the form

`<li><a{% if selected=="NAME_LOWERCASE" %} class="selected"{% endif %} href="NAME_TITLECASE.html">NAME_USUAL</a></li>`

(For example, `<li><a{% if selected=="suggestions" %} class="selected"{% endif %} href="Suggestions.html">Suggestion Form</a></li>`)

### 2. Create the `html` template file at `html/name.html`

You'll probably want to start with
```
{% extends "base.html" %}
{% set name='NAME_TITLECASE' %}
{% set selected='NAME_LOWERCASE' %}
{% block content %}
{% endblock %}
```
where, e.g., `NAME_TITLECASE` is `Home` and `NAME_LOWERCASE` is `home`.

Your content will go in between `{% block content %}` and `{% endblock %}`.

### 3. Create the `txt` file at `text/name.txt`

If you don't need any content to be easily updated via a textfile (e.g., the committees list in `Documents.html` or the members list in `Members.html`), this can be left empty (n.b., you still should create the file, though).

### 4. Create the `py` file at `python/name.py`

Once again, if you don't need the content to be dynamically generated with python variables, this can be a simple file containing only the following lines
```
def main():
  return {}
```

### 5. Add your changes to the git repository

(See **Making Changes** to see how)

## Installation

1. Download the git repository
2. Navigate to the location in your terminal
3. run `pip install -r requirements.txt`

## Internal Details
### Folder Structure
For every page with name `name`, there is a

* `python/name.py` file
* `html/name.html` file
* `text/name.txt` file

### Makefile
The `makefile` in the root directory internally runs `python render.py PageName` for every page name. `render.py` reads the template at `html/name.html` and renders it using the variable dictionary returned by the `main` method of `python/name.py`.
