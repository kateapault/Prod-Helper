import dropbox
import tokensandkeys

def main():
# connect to dropbox
    dbx = dropbox.Dropbox(tokensandkeys.my_token)

#get part number to look up
    part_number = input("What part number are you looking for? ")

# search for files of that part number in the Production folder
    search_function = dbx.files_search("/ZipFlyer Team Folder/Production Files", part_number)

#check to see if there are any files of the part number
#search_function.matches is a list. If it is empty, there are no files of that part number
    if len(search_function.matches) > 0:
        print("Found it!")
    else:
        print("Not Here")
# create folder for part
        #dropbox.files.CreateFolderArg("/ZipFlyer Team Folder/1. Engineering/Kate's Work Folder/hurrah/")
 
        #dropbox.files.create_folder("/ZipFlyer Team Folder/1. Engineering/Kate's Work Folder/yas/")
        #dbx.files_copy("/ZipFlyer Team Folder/1. Engineering/Kate's Work Folder/test", "/ZipFlyer Team Folder/1. Engineering")
        # WHAT IS '"ROUTE" OBJECT IS NOT CALLABLE'
        #dropbox.files.CreateFolderArg("/ZipFlyer Team Folder/1. Engineering/Kate's Work Folder/New Dropbox Folder")
    file_locs = file_finder(part_number,'.txt')
    # for each file loc
        # move that file to created folder

# search for files of type
def file_finder(part_num, *file_ext):
    all_part_files = dbx.files_search("/ZipFlyer Team Folder", part_num)
    # extract file location & file type
    # for each file type requested
        # add locations to list
    #return list of locations
    pass

if __name__ == '__main__':
    app.run()