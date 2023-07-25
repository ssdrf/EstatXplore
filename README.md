# EurostatXplore
A terminal-based Eurostat data previewer.


## Setup


###### Step 1: Clone the repository
git clone https://github.com/{name/repo}.git

###### Step 2: Navigate into the directory
cd YourRepositoryName

###### Step 3: Make `give` executable
chmod +x give

###### Step 4: Create a symbolic link
ln -s /full/path/to/your/directory/give /usr/local/bin/estat

">>>" estat give plot "TIPSII40" "DE" 0 10 </br>

![Estat](https://github.com/ssdrf/EurostatXplore/assets/138875022/7f89ef2b-80e5-42fe-b332-2fb4e9004f76)

###### Commands:
{plot} "code-string" "geo-string" {col} {period} </br>
{search} "search-string" </br>
{show} "code-string"
