
![Logo](https://user-images.githubusercontent.com/23452745/140636507-c2104cca-2f2a-45a1-87e1-a9e6b73f66a9.png)

![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue?style=flat&logo=python&logoColor=white)
# Table of Contents

- [Raziel](#raziel)
  * [Features](#features)
  * [Getting Started](#getting-started)
  * [How to use Raziel](#how-to-use-raziel)
      - [To run Raziel](#to-run-raziel)
      - [To see Raziel's help message](#to-see-raziels-help-message)
      - [To search](#to-search)
      - [To see Raziel tools' help message](#to-see-raziel-tools-help-message)
      - [List all tools you can find in Raziel](#list-all-tools-you-can-find-in-raziel)
      - [See the help message for a tool in Raziel](#see-the-help-message-for-a-tool-in-raziel)
      - [Print all info about a tool](#print-all-info-about-a-tool)
      - [See the tool's description](#see-the-tool-s-description)
      - [Find what the latest stable release of a tool is](#find-what-the-latest-stable-release-of-a-tool-is)
      - [Print the tool's official site](#print-the-tools-official-site)
      - [Print a tool's repository site(s)](#print-a-tools-repository-sites)
      - [Bookmark a tool](#bookmark-a-tool)
      - [Remove a tool from bookmarks](#remove-a-tool-from-bookmarks)
      - [Show help messsage on tool installation guide](#show-help-messsage-on-tool-installation-guide)
      - [Show how to install a tool](#show-how-to-install-a-tool)
      - [Show how to use a tool](#show-how-to-use-a-tool)
      - [List all known errors a tool has](#list-all-known-errors-a-tool-has)
      - [Show help message for the pros & cons of a tool](#show-help-message-for-the-pros--cons-of-a-tool)
      - [Show pros & cons of a tool](#show-pros--cons-of-a-tool)
      - [Show only the pros of a tool](#show-only-the-pros-of-a-tool)
      - [Show only the cons of a tool](#show-only-the-cons-of-a-tool)
      - [See what are the guides Raziel has](#see-what-are-the-guides-raziel-has)
      - [Show notes help message](#show-notes-help-message)
      - [Create a new note](#create-a-new-note)
      - [List all notes created](#list-all-notes-created)
      - [Show help message for bookmarks](#show-help-message-for-bookmarks)
      - [Show your bookmarks](#show-your-bookmarks)
      - [Add/Remove multiple tools/guides from bookmarks](#addremove-multiple-toolsguides-from-bookmarks)
  * [Future Plans](#future-plans)
  * [Support & Feedback](#support--feedback)
  * [Authors](#authors)


# Raziel
## About
Raziel is a Python CLI tool that aims to resolve these issues by being a free all-in-one tool that is easy to navigate and use, and in the future, gain its own community who will continue to support and bring out its full potential.
Raziel was created to address some of the problems newcomers face which includes, but not limited to, learning outdated or false information, finding sources that requires them to pay to read or contradicts one another and not knowing which is right, encountering documentations that just leaves readers even more puzzled, or not being able to find any information at all. It aims to become a centralised point of information that is easy to use, free and is a database that contains multiple forensic tools and information.

See below for our video showcasing Raziel below.


<https://user-images.githubusercontent.com/33174163/140646690-2e82b407-9eb8-4e8c-8d32-76d1ede5c3fc.mp4>



## Some Features
Quick search for information

<https://user-images.githubusercontent.com/33174163/140648844-35ec2c26-7970-4ef2-ae14-71720222857d.mp4>

Running shell command via the suggestions search gives

<https://user-images.githubusercontent.com/33174163/140648807-78f63606-6a64-401f-b35c-80a0fd5b4864.mp4>

Learning about a tool

<https://user-images.githubusercontent.com/33174163/140648665-9e54bf0b-9d8b-4da8-99e7-44b628adbc44.mp4>

Seeing the pros & cons of a tool

<https://user-images.githubusercontent.com/33174163/140648782-27e358cf-a024-4826-81b8-d5f805ec383a.mp4>

Learning a new topic or revising with guides

<https://user-images.githubusercontent.com/33174163/140648715-26da7f72-b9aa-4995-9a77-3f370acab318.mp4>

Taking notes

<https://user-images.githubusercontent.com/33174163/140648547-a1630e70-0350-4471-b523-b0b0976b06b7.mp4>

Bookmarking tools/chapters in the guides

<https://user-images.githubusercontent.com/33174163/140648603-a23dfc0d-77dd-43d7-8902-039e160aa5bb.mp4>

Multiple ways of running Raziel (python raziel.py & python raziel.py args)

<https://user-images.githubusercontent.com/33174163/140651266-3bd6348b-632b-492c-b2cd-b9ab6f9e201d.mp4>



## Getting Started

Clone the project or download the repository as a ZIP

```bash
git clone https://github.com/Yggralith0/Raziel.git
```
_OR_

![Download ZIP](<https://user-images.githubusercontent.com/23452745/140635242-f9f793b3-1461-45bb-9af1-842e13960029.png>)


Go to the project directory

```bash
cd wherever_you_cloned_the_project_to/Raziel
```

Install dependencies

```bash
 pip install -r requirements.txt
```


## How to use Raziel
#### To run Raziel
```bash
python raziel.py
```
Output:
![Run Raziel](<https://user-images.githubusercontent.com/23452745/140635510-11e46716-e994-4252-8d29-6db70eb1d714.png>)

---
#### To see Raziel's help message
```bash
python raziel.py {--help | -h}
```
Output
![Raziel Help](<https://user-images.githubusercontent.com/23452745/140635588-3004e7d2-72bb-40d3-9671-38a1fa64b72c.png>)

---
#### To search 
Select "1) Search" in the main menu
![Search](<https://user-images.githubusercontent.com/23452745/140637528-44de6cac-db40-4af0-af28-d4fa3377ee38.png>)

_OR_

```bash
python raziel.py search
```
Output
![search_1](<https://user-images.githubusercontent.com/23452745/140637893-37fdb808-134f-45c8-8f23-6af7062ae68a.png>)

Start searching
![searching](<https://user-images.githubusercontent.com/23452745/140637943-54b68029-f7f6-4f13-8d10-383610b52105.png>)

---
#### To see Raziel tools' help message
```bash
python raziel.py tools {--help | -h}
```
Output
![raziel_tools_help](<https://user-images.githubusercontent.com/23452745/140638184-f9fa853e-8495-4c4f-b992-96d90c1b78ad.png>)

---
#### List all tools you can find in Raziel
Select "2) Tools" in the main menu
![list_tools](<https://user-images.githubusercontent.com/23452745/140638268-a41f63e3-bfca-4e2f-84ab-2a79f426b9dc.png>)

Output
![select_tool](<https://user-images.githubusercontent.com/23452745/140638336-a3c5ce4f-c189-410c-b4e5-12ca6e7ed7b7.png>)

_OR_

```bash
python raziel.py tools {--list | -ls}
```
Output
![list_tools](<https://user-images.githubusercontent.com/23452745/140638453-df662550-bc09-4e5f-946e-18b04212b507.png>)

---
#### See the help message for a tool in Raziel
```bash
python raziel.py tools tool_name {--help | -h}
```
Output
![tool help](<https://user-images.githubusercontent.com/23452745/140641202-6af60e87-492c-46b3-aab0-4f5abd28c75f.png>)

#### Print all info about a tool
Select a tool
![select_tool](<https://user-images.githubusercontent.com/23452745/140638336-a3c5ce4f-c189-410c-b4e5-12ca6e7ed7b7.png>)

Select "1) About"
![tool_selected_about](<https://user-images.githubusercontent.com/23452745/140638746-36d33df2-5aff-4377-be9c-927f1961a192.png>)

_OR_
```bash
python raziel.py tools tool_name tool_name {--about | -a} 
```
- Note: The 2nd `tool_name` is the tool name itself 
    - E.g. `python raziel.py tools Chainsaw --about`
Output
![about_tool](<https://user-images.githubusercontent.com/23452745/140638780-af34b30b-fe98-4b84-afc1-c48a28b414d4.png>)

---
#### See the tool's description
```bash
python raziel.py tools tool_name tool_name {--description | -d}
```
Output
![tool description](<https://user-images.githubusercontent.com/23452745/140639012-48fae26c-6716-4c78-9f0d-16ebc04e3792.png>)

---
#### Find what the latest stable release of a tool is
```bash
python raziel.py tool_name tool_name {--latest | -lsr}
```
Output
![lsr](<https://user-images.githubusercontent.com/23452745/140639160-5753e404-335f-4be9-accb-1655173dcaf5.png>)

---
#### Print the tool's official site
```bash
python raziel.py tool_name tool_name {--official_site | -os}
```
Output
![tool_official_site](<https://user-images.githubusercontent.com/23452745/140639403-a35d291f-64c9-48bf-a9c6-3d81cf5b8034.png>)
---
#### Print a tool's repository site(s)
```bash
python raziel.py tool_name tool_name {--repository | -r}
```
Output
![repo](<https://user-images.githubusercontent.com/23452745/140639474-27bc14ed-65f5-428b-b59a-dadc930573b1.png>)

---
#### Bookmark a tool
Select "7) Bookmark this tool"
![bookmark_tool](<https://user-images.githubusercontent.com/23452745/140640633-7fc9964b-1f93-49c3-82ec-2f6a617583ad.png>)
- If tool already bookmarked, will show "7) Remove bookmark for this tool"
_OR_
```bash
python raziel.py tool_name tool_name --bookmark
```

---
#### Remove a tool from bookmarks
Select "7) Remove bookmark for this tool"
![unbookmark tool](<https://user-images.githubusercontent.com/23452745/140640709-eed9cafd-b226-4a1e-8655-8800132eb995.png>)
- If tool has not been bookmarked, will show "7) Bookmark this tool"
_OR_
```bash
python raziel.py tool_name tool_name --no-bookmark
```

---
#### Show help messsage on tool installation guide
![install tool](<https://user-images.githubusercontent.com/23452745/140640055-7c6237f9-50d7-40bf-9ad2-9dd357523d12.png>)

--- 
#### Show how to install a tool
Select "2) How to install"
![select how to install](<https://user-images.githubusercontent.com/23452745/140644153-bf6d17fe-7c28-495c-9627-5969af880f78.png>)

Select the platform you are intending to install the tool on
![platform_install](<https://user-images.githubusercontent.com/23452745/140640792-2460892f-66b2-4bc1-a6b5-b1c61ab65068.png>)

_OR_
```bash
python raziel.py tools tool_name tool_name install {--platform | -p} {Windows | Linux | Mac}
```
Output
![install on windows](<https://user-images.githubusercontent.com/23452745/140640975-5c47209c-fe19-4b79-8d96-1dce78ffc60f.png>)

---
#### Show how to use a tool
Select "3) How to use"
![how to use](<https://user-images.githubusercontent.com/23452745/140641257-c797c9a2-7b5f-4c46-a41b-573824bb0999.png>)

_OR_
```bash
python raziel.py tools tool_name tool_name how_to_use {--help | -h}
```
- If the tool has more than 1 feature, Raziel will ask user to select which feature he/she wants to learn about
  ![select feature](<https://user-images.githubusercontent.com/23452745/140641324-9167d8dc-0c22-4e49-bf52-6c5e918e9e3a.png>)

---
#### List all known errors a tool has
Select "4) Erros & how to fix"
![error](<https://user-images.githubusercontent.com/23452745/140641449-b5e4f6ec-b4f8-4bc8-b2ac-ccb8c5aba4f5.png>)

_OR_
```bash
python raziel.py tools tool_name tool_name errors
```
Output
![list of errors](<https://user-images.githubusercontent.com/23452745/140641497-006555b1-26af-4700-9a95-916411276da0.png>)

Select an error to know how to fix it
![fix](<https://user-images.githubusercontent.com/23452745/140641584-1ce52eda-92f3-43d9-890e-9f38581715c5.png>)

---
#### Show help message for the pros & cons of a tool
```bash
python raziel.py tools tool_name tool_name pros_cons {--help | -h}
```
Output
![pros cons help](<https://user-images.githubusercontent.com/23452745/140641735-3583f4c7-f3a2-4c29-9873-2196d00add74.png>)

---
#### Show pros & cons of a tool
Select "5) Pros & Cons"
![pros_cons](<https://user-images.githubusercontent.com/23452745/140641804-bca414b2-2fdf-47a2-986f-75668dbda26b.png>)

_OR_
```bash
python raziel.py tools tool_name tool_name pros_cons
```
_OR_
```bash
python raziel.py tools tool_name tool_name pros_cons both
```
Output
![pros_cons_output](<https://user-images.githubusercontent.com/23452745/140641879-6e982c01-a79c-486e-a063-d7a92e13bae7.png>)

---
#### Show only the pros of a tool
```bash
python raziel.py tools tool_name tool_name pros_cons pros
```
Output
![pros](<https://user-images.githubusercontent.com/23452745/140641967-062b05d3-bf6b-421f-ae30-628b6dc5bbb9.png>)

---
#### Show only the cons of a tool
```bash
python raziel.py tools tool_name tool_name pros_cons cons
```
Output
![cons](<https://user-images.githubusercontent.com/23452745/140642077-5bf5d1cb-ffa5-4071-bff0-f51b757cdce8.png>)

---
#### See what are the guides Raziel has
Select "3) Guides"
![select guide](<https://user-images.githubusercontent.com/23452745/140642270-67a9d118-7276-4959-90e0-7bec00f9a4d8.png>)

_OR_
```bash
python raziel.py guides
```
Output
![guides](<https://user-images.githubusercontent.com/23452745/140642309-751fb3c4-8f4c-4b47-bda4-db6eec035c6e.png>)

After selecting a guide, user will be asked to select a chapter to read
![chapters](<https://user-images.githubusercontent.com/23452745/140642359-390d1d44-d34f-45fc-9ae3-6a8cf0f76020.png>)

User can then choose to read either the whole chapter or a subchapter of the chosen chapter
![subchapters](<https://user-images.githubusercontent.com/23452745/140642394-76b5b269-bb86-439c-9e3d-b1dbad7f311f.png>)

Output
![subchapter_selected](<https://user-images.githubusercontent.com/23452745/140642424-bcc23bcf-58d4-4112-837e-bb74c4208576.png>)

---
#### Show notes help message
```bash
python raziel.py notes {--help | -h}
```
![notes_help](<https://user-images.githubusercontent.com/23452745/140642493-d07874eb-c5a2-4d23-b6ee-c91f306bfcea.png>)

---
#### Create a new note
Select "4) Notes"
![select_notes](<https://user-images.githubusercontent.com/23452745/140642592-f082c6f8-9332-40b2-9823-444eb808034a.png>)

Select "Create a new note"
![new note](<https://user-images.githubusercontent.com/23452745/140642617-6e6977cb-5550-4966-a432-cdfe0c5912bb.png>)

_OR_
```bash
python raziel.py notes {--new | -n}
```
Output
![text editor](<https://user-images.githubusercontent.com/23452745/140642672-e8a95a3c-e261-4928-bbea-b44f36b42469.png>)

---
#### List all notes created
- Note (no pun intended): Raziel will only show notes that are in the "Raziel Notes" folder
Select "2) See existing notes"
![see_notes](<https://user-images.githubusercontent.com/23452745/140642747-9594280b-9251-427e-b803-03f004dc3c19.png>)

_OR_
```bash
python raziel.py notes {--list | -ls}
```
Output
![list_notes](<https://user-images.githubusercontent.com/23452745/140642880-fff46c75-eddc-488a-842f-6ced6f819fea.png>)
- Selecting the note will launch it in a text editor
If your note isn't listed, select "I can't find the file I'm looking for"
![find note](<https://user-images.githubusercontent.com/23452745/140642991-72917f8d-565d-44f3-88c0-a8867f13ec49.png>)

You will then be prompted to enter the path to your note
![filepath](<https://user-images.githubusercontent.com/23452745/140643074-c9f89bf1-06e3-4021-9273-17a753a3cc46.png>)

---
#### Show help message for bookmarks
```bash
python raziel.py bookmarks {--help | -h}
```
![bookmarks help](<https://user-images.githubusercontent.com/23452745/140643497-13041186-513b-4a5d-85f9-5460fe4af81f.png>)

---
#### Show your bookmarks
Select "5) Bookmarks"
![select_bookmarks](<https://user-images.githubusercontent.com/23452745/140643387-71e1aabe-90a6-4569-aa56-22f5c97f2a32.png>)

Select "1) See my bookmarks"
![see_bookmarks](<https://user-images.githubusercontent.com/23452745/140643411-f9ea511f-2287-4e1f-8ada-9e73f2d3ae03.png>)

_OR_
```bash
python raziel.py bookmarks {--list | -ls}
```
Output
![bookmarks list](<https://user-images.githubusercontent.com/23452745/140643603-7f991247-f6a6-471e-8a32-5ad004b05ba8.png>)
- Selecting a bookmark will bring you to its info screen

---
#### Add/Remove multiple tools/guides from bookmarks
Select "2) Edit my bookmarks"
![edit_bookmarks](<https://user-images.githubusercontent.com/23452745/140643697-3513d6f7-012f-4320-97a6-1e520409dfae.png>)

_OR_
```bash
python raziel.py bookmarks {--edit | -e}
```
Output
![editing bookmarks](<https://user-images.githubusercontent.com/23452745/140643813-ef8795c4-c40f-4c3e-87f4-b94df23f2ed9.png>)
## Future Plans

- Improved coding & performance
- AI support for searching
- Storing values in a remote database instead of local JSON files
- GUI version
- Mobile app with voice assistant


## Support & Feedback
Found a bug or want to add to Raziel?\
Email <isaacchoojh@gmail.com> or join our [Discord](<https://discord.gg/CCsnqwzcm8>)!
## Authors
- [Brandon Lee](<https://github.com/brandonlee3355>)

  ![Your Repository's Stats](<https://github-readme-stats.vercel.app/api?username=brandonlee3355&show_icons=true>)
- [Dennis](<https://github.com/Watcher97>)
  
  ![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=Watcher97&show_icons=true)
- [Isaac](<https://github.com/Yggralith0>)

  ![Your Repository's Stats](<https://github-readme-stats.vercel.app/api?username=Yggralith0&show_icons=true>)
- [Qiao Yan](<https://github.com/Yukikozen>)

  ![Your Repository's Stats](<https://github-readme-stats.vercel.app/api?username=ushiococo&show_icons=true>)

