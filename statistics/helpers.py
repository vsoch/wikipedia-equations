# helpers.py, useful helper functions for wikipedia analysis
# We want to represent known symbols (starting with //) as words, the rest characters



def save_pretty_json(dict_obj,output_file):
    with open(output_file, 'w') as outfile:
        json.dump(dict_obj,outfile)

def write_file(filename, content, mode="w"):
    with open(filename, mode) as filey:
        if isinstance(content, list):
            for item in content:
                filey.writelines(content)
        else:
            filey.writelines(content)
    return filename

def get_attribute(entry, name, default=[]):
    '''A helper to get an attribute from an object, if it exists.
       If not, return some default.'''
    try:
        if hasattr(entry, name):
            return getattr(entry, name)    
    except KeyError:
        pass
    return default


def extract_tokens(tex):
    '''walk through a LaTeX string, and grab chunks that correspond with known
       identifiers, meaning anything that starts with \ and ends with one or
       more whitespaces, a bracket, a ^ or underscore.
    '''
    regexp = r'\\(.*?)(\w+|\{|\(|\_|\^)'
    tokens = []
    while re.search(regexp, tex) and len(tex) > 0:
        match = re.search(regexp, tex)
        # Only take the chunk if it's starting at 0
        if match.start() == 0:
            tokens.append(tex[match.start():match.end()])
            # And update the string
            tex = tex[match.end():]
        # Otherwise, add the next character to the tokens list
        else:
            tokens.append(tex[0])
            tex = tex[1:]

    # When we get down here, the regexp doesn't match anymore! Add remaining
    if len(tex) > 0:
        tokens = tokens + [t for t in tex]
    return tokens

def update_method_name(methods, old_name, new_name):
    '''update the set by removing an old name (usually a disambuguation error)
       with a new name

       Parameters
       ==========
       methods: the set of methods
       oldName: the name to remove
       newName: the name to add
    '''
    if old_name in methods:
        methods.remove(old_name)
    methods.add(new_name)
    return methods

