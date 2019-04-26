#!/usr/bin/env python
# -*- coding: utf-8 -*-

def generate_web_form(field_lsit):
    generated_fields = "\n".join(map(
        lambda x: '{0}:<br><input type="text" name="{0}"><br>'.format(x), field_lsit
    ))

    return "<form>{fields}</form>".format(fields=generated_fields)


def build_html_form(fields):
    with open("form_file.html", 'w') as f:
        f.write(
            "<html><body>{}</body></html>".format(generate_web_form(fields))
        )


if __name__ == '__main__':
    fields = ["name", "age", "email", "telephone"]
    build_html_form(fields)
