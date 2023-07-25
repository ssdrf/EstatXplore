# EurostatXplore
A terminal-based Eurostat data previewer.


## Setup


###### Step 1: Clone the repository
git clone https://github.com/YourGitHubUsername/YourRepositoryName.git

###### Step 2: Navigate into the directory
cd YourRepositoryName

###### Step 3: Make `give` executable
chmod +x give

###### Step 4: Create a symbolic link
ln -s /full/path/to/your/directory/give /usr/local/bin/estat

">>>" estat give plot "TIPSII40" "DE" 0 10 </br>

![Estat](https://github.com/ssdrf/EstatXplore/assets/138875022/b800aa4a-7cdd-4ddb-9a2b-b41033bc457b)
###### Commands:
{plot} "code-string" "geo-string" {col} {period} </br>
{search} "search-string" </br>
{show} "code-string"
