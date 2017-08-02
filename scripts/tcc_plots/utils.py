def filename_from_title(title, extension):
    return '../attachments/' + title.lower().replace(' ', '_') + "." + extension