def filename_from_title(title, extension):
    return '../plots/' + title.lower().replace(' ', '_') + "." + extension