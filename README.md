#### Overview

Pulls search terms from Google and writes those keywords to a plaintext file. The search terms are based off the Google Trends RSS feed. The keywords themselves are the most popular ones for that specific day, _i.e._ the day you ran it.

#### Learning outcomes

1. Utilise XML data

#### To do

1. Implement perf measurement
2. Append date-time to filename when writing

#### Important notes

If **local_folder_path** is set incorrectly and you do not have read/write permissions to the folder _the script will not work_. You must replace the contents of this string with your own directory, _and it must exist before running_:  

    local_folder_path = "/xyz/enter-local-path-here/"

Please make sure there is an _ending_ forward slash. If you're a Windows user backslashes will need to be replaced by forward slashes.  

As there were changes in Python 3.7 on macOS, Keychain Access for certificates are depreciated and it's replaced by OpenSSL. The following line is required to ignore the integrity check of the URL:

    ssl._create_default_https_context = ssl._create_unverified_context

You can read more about the changes [here](https://docs.python.org/3/whatsnew/3.7.html#ssl).

Please check the certificate yourself so you know that it's authentic.

#### The code

Hopefully most of the code is self-explanatory. I've added some explanations here for further clarification:

    rss_locale = "NZ"

This is the locale for the Google Trends feed. The default is New Zealand (**NZ**), however it can be changed to other regions (e.g. **US** for the United States, or **AU** for Australia).

    urllib.request.urlretrieve(google_trends_url, "{0}/{1}".format(local_folder_path, xml_output_file))

This retrieves the data from the RSS feed and writes it to XML.

    element_tree = xml_tree.parse("{0}/{1}".format(local_folder_path, xml_output_file))

This parses the XML and assigns it to **element_tree**.

    tree_root = element_tree.getroot()

This returns the root element of the tree and assigns it to **tree_root**.

    for keyword in tree_root.iter("title"):
        search_terms.append(keyword.text)

This recursively parses the title column for each search term. On each iteration the search term is added to the **search_terms** list.

    popular_searches = "\n".join(search_terms)

This creates a string and inserts each seach term on a new line.

    output = open("{0}/{1}".format(local_folder_path, plaintext_output_file), "w+")
    output.write(popular_searches)
    output.close()

This creates the plaintext file, writes the data to it, then closes it from memory.

    os.remove("{0}/{1}".format(local_folder_path, xml_output_file))

This removes the XML file from disk. This can be commented out if you wish to keep it.