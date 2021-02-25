# Experiencing M I S

Ninth Edition

<img src="img/kroenke_emis9e_ppt_050.jpg" width=500px />

__Chapter 5__

Database Processing

Slides in this presentation contain hyperlinks\. JAWS users should be able to get a list of links by using INSERT\+F7

Copyright © 2021\, 2019\, 2017 Pearson Education\, Inc\. All Rights Reserved

# “The tricky part is getting the computer to correctly identify the inventory item.”

<span style="color:#000000">eHermes is using Google’s image classifier API to identify images that customers upload\.</span>

<span style="color:#000000">Costs a few dollars per 1000 images searched</span>

<span style="color:#000000">Need new data storage</span>

<span style="color:#000000">Need redesigned database</span>

<span style="color:#000000">Need new DBMS</span>

<span style="color:#000000">Will be sending and receiving data from multiple data sources</span>

<span style="color:#000000">MongoDB for tracking image files?</span>

# Study Questions

__5\-1__  <span style="color:#000000">Why do you need to know about databases?</span>

__5\-2__  <span style="color:#000000">What is a database?</span>

__5\-3__  <span style="color:#000000">What is a database management system \(D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S\)?</span>

__5\-4__  <span style="color:#000000">How do database applications make databases more useful?</span>

__5\-5__  <span style="color:#000000">How can eHermes benefit from a database system?</span>

__5\-6__  <span style="color:#000000">What are nontraditional D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S products?</span>

# Why Use a Database?

5\-1 Why do you need to know about databases?

<span style="color:#000000">Can database technology facilitate your project goals?</span>

<span style="color:#000000">Databases are ubiquitous in commerce\.</span>

<span style="color:#000000">How to turn data into useful information\.</span>

<span style="color:#000000">Business adaptation requires changing database structure\.</span>

<span style="color:#000000">As a future business professional\, you might need to build a database\.</span>

# What is the Purpose of a Database?

* 5\-1 Why do you need to know about databases?
* <span style="color:#000000">Organize and keep track of things\.</span>
* <span style="color:#000000">Keep track of multiple themes\.</span>
* <span style="color:#000000">General rule:</span>
  * <span style="color:#000000">Single theme—store in a spreadsheet\.</span>
  * <span style="color:#000000">Multiple themes—use a database\.</span>
  * <span style="color:#000000">What’s a theme?</span>
    * <span style="color:#000000">Ex: student grades\, student emails\, student office visits\.</span>

# A List of Student Grades Presented in a Spreadsheet – Single Theme

5\-1 Why do you need to know about databases?

__Figure 5\-1__ A List of Student Grades Presented in a Spreadsheet

<img src="img/kroenke_emis9e_ppt_051.jpg" width=500px />

# Student Data Form for a Database Application

5\-1 Why do you need to know about databases?

__Figure 5\-2__ Student Data Shown in a Form from a Database

<img src="img/kroenke_emis9e_ppt_052.jpg" width=500px />

# What is a Database?

5\-2 What is a database?

<span style="color:#000000"> __Figure 5\-3__ </span>  <span style="color:#000000">Student Table \(also called a file\)</span>

<img src="img/kroenke_emis9e_ppt_053.jpg" width=500px />

# Hierarchy of Data Elements

5\-2 What is a database?

__Figure 5\-4__ Hierarchy of Data Elements

<img src="img/kroenke_emis9e_ppt_054.jpg" width=500px />

# Components of a Database

5\-2 What is a database?

__Figure 5\-5__ Components of a Database

<img src="img/kroenke_emis9e_ppt_055.jpg" width=500px />

# Example of Relationships Among Rows

5\-2 What is a database?

__Figure 5\-6__ Example of Relationships Among Rows

<img src="img/kroenke_emis9e_ppt_056.jpg" width=500px />

# Sample of Access Metadata

5\-2 What is a database?

__Figure 5\-7__ Sample Metadata \(in Access\)

<img src="img/kroenke_emis9e_ppt_057.jpg" width=500px />

# Database Management System (D B M S)

5\-3 What is a database management system \(DBMS\)?

<span style="color:#000000">Functions of a D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S</span>

  * <span style="color:#000000">Creating the Database and its structures</span>
  * <span style="color:#000000">Processing the database</span>
  * <span style="color:#000000">Administering the database</span>

* <span style="color:#000000">Licensed from vendors</span>
  * <span style="color:#000000">I</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M\, Microsoft\, Oracle\, and others\.</span>
    * <span style="color:#000000">D</span>  <span style="color:#000000">B2\, Access\, S</span>  <span style="color:#000000">Q</span>  <span style="color:#000000">L Server\, Oracle Database\.</span>
* <span style="color:#000000">Open source</span>
  * <span style="color:#000000">My</span>  <span style="color:#000000">S</span>  <span style="color:#000000">Q</span>  <span style="color:#000000">L: License\-free for most applications\.</span>

# Processing the Database (1 of 2)

5\-3 What is a database management system \(DBMS\)?

<span style="color:#000000">Creating the database \(see form in Figure 5\-7\)</span>

<span style="color:#000000">Modifying the database structure \(see Figure 5\-8\)</span>

<span style="color:#000000">D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S Process Operations</span>

  * <span style="color:#000000">Read</span>
  * <span style="color:#000000">Insert</span>
  * <span style="color:#000000">Modify</span>
  * <span style="color:#000000">Delete data</span>

# Adding a New Column to a Table (in Access 2019)

5\-3 What is a database management system \(DBMS\)?

__Figure 5\-8__ Adding a New Column to a Table \(in Access\)

<img src="img/kroenke_emis9e_ppt_058.jpg" width=500px />

<span style="color:#000000"> __Source__ </span>  <span style="color:#000000">: Microsoft Access 2019</span>

# Processing the Database (2 of 2)

* 5\-3 What is a database management system \(DBMS\)?
* <span style="color:#000000">Structured Query Language—S</span>  <span style="color:#000000">Q</span>  <span style="color:#000000">L \(see\-quell\)</span>
  * <span style="color:#000000">International standard</span>
  * <span style="color:#000000">Used by nearly all D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S</span>
* <span style="color:#000000">S</span>  <span style="color:#000000">Q</span>  <span style="color:#000000">L Example</span>
* <span style="color:#000000">INSERT INTO Student</span>
  * <span style="color:#000000">\(\[Student Number\]\, \[Student Name\]\, H</span>  <span style="color:#000000">W1\, H</span>  <span style="color:#000000">W2\, MidTerm\)</span>
* <span style="color:#000000">VALUES \(1000\, ‘Franklin\, Benjamin’\, 90\, 95\, 100\);</span>

# Slick Analytics (1 of 2)

* <span style="color:#000000">So What?</span>
* <span style="color:#000000">C</span>  <span style="color:#000000">I</span>  <span style="color:#000000">O</span>  <span style="color:#000000">s are looking to merge the</span>  <span style="color:#000000"> __storage__ </span>  <span style="color:#000000">and</span>  <span style="color:#000000"> __analysis__ </span>  <span style="color:#000000">of cloud\-based data into one synergistic operation\.</span>
* <span style="color:#000000">Laredo Petroleum\.</span>
  * <span style="color:#000000">Old approach used numerous spreadsheets and manual calculations\.</span>
  * <span style="color:#000000">Value of data diminished due to the time it took to analyze the data\.</span>
  * <span style="color:#000000">New approach uses cloud storage and cloud analytics\.</span>

* So What?
* <span style="color:#000000">Laredo Petroleum\.</span>
  * <span style="color:#000000">Needs to know when it should clean chemical deposits in its wells\.</span>
  * <span style="color:#000000">Cloud storage and analytics improved scalability\, robust data analysis\, and data accessibility\.</span>
* <span style="color:#000000">Cloud analytics will grow by 46 percent through 2020\.</span>
* <span style="color:#000000">Security and privacy concerns are drawbacks to cloud services\.</span>

# Administering the Database

5\-3 What is a database management system \(DBMS\)?

<span style="color:#000000">Set up security system\, user accounts\, passwords\, permissions\, limits for processing\.</span>

<span style="color:#000000">Limit user permissions\.</span>

<span style="color:#000000">Back up database\, improve performance of database applications\, remove unwanted data\.</span>

# Summary of Database Administration Tasks (1 of 2)

5\-3 What is a database management system \(DBMS\)?

__Figure 5\-9__ Summary of Database Administration \(DBA\) Tasks \(continues on next slide\)

5\-3 What is a database management system \(DBMS\)?

__Figure 5\-9__ Summary of Database Administration \(DBA\) Tasks \(con’t\.\)

# Forms, Queries, Reports, and Applications

5\-4 How do database applications make databases more useful?

# Users Accessing Databases

5\-4 How do database applications make databases more useful?

<span style="color:#000000"> __Figure 5\-10__ </span>  <span style="color:#000000">Processing Environment of a Traditional Database Application System</span>

<img src="img/kroenke_emis9e_ppt_059.jpg" width=500px />

# Example of a Student Report

5\-4 How do database applications make databases more useful?

__Figure 5\-11__ Example of a Student Report

<img src="img/kroenke_emis9e_ppt_0510.jpg" width=500px />

# Query Example

5\-4 How do database applications make databases more useful?

<span style="color:#000000"> __Figure 5\-12A__ </span>  <span style="color:#000000">Sample Query Form Used to Enter Phrase for Search</span>

<span style="color:#000000"> __Figure 5\-12B__ </span>  <span style="color:#000000">Sample Query Results of Query Operation</span>

<img src="img/kroenke_emis9e_ppt_0511.png" width=500px />

<span style="color:#000000"> __Source__ </span>  <span style="color:#000000">: Microsoft Corporation</span>

<img src="img/kroenke_emis9e_ppt_0512.png" width=500px />

<span style="color:#000000"> __Source__ </span>  <span style="color:#000000">: Microsoft Access 2019</span>

# Browser Forms, Reports, Queries, and Applications

5\-4 How do database applications make databases more useful?

<span style="color:#000000"> __Figure 5\-13__ </span>  <span style="color:#000000">Processing Environment of Browser\-Based Database Applications</span>

<img src="img/kroenke_emis9e_ppt_0513.jpg" width=500px />

# Account Creation Browser Form

5\-4 How do database applications make databases more useful?

__Figure 5\-14__ Microsoft Office 365 User Account Form

<img src="img/kroenke_emis9e_ppt_0514.jpg" width=500px />

# Browser Report

5\-4 How do database applications make databases more useful?

__Figure 5\-15__ Browser Report for SharePoint Site

<img src="img/kroenke_emis9e_ppt_0515.jpg" width=500px />

# Multiuser Processing Problem

5\-4 How do database applications make databases more useful?

<span style="color:#000510">Andrea reads available tickets record showing 2 tickets\.</span>

<span style="color:#000510">5\. Andrea proceeds to checkout\. Someone will  be disappointed\.</span>

<span style="color:#000510">3\. Andrea puts both in shopping basket\, but delays checking out\.</span>

<span style="color:#000510">Jeffrey reads same record showing 2 available tickets\.</span>

<span style="color:#000510">Jeffrey puts both in shopping basket and checks out  before Andrea\.</span>

# A Database System at eHermes

* 5\-5 How can eHermes benefit from a database system?
* <span style="color:#000000">Speed up the process of inventorying new items received from sellers\.</span>
  * <span style="color:#000000">“Can we add a new item’s entry in our database using a photo and Google’s image classifier to recognize the item\, search for product information from multiple sources\, and complete the database entry?”</span>
* <span style="color:#000000">Choices</span>
  * <span style="color:#000000">Store images on a file server and keep metadata about each image in a relational database to query with S</span>  <span style="color:#000000">Q</span>  <span style="color:#000000">L\.</span>
  * <span style="color:#000000">Use No</span>  <span style="color:#000000">S</span>  <span style="color:#000000">Q</span>  <span style="color:#000000">L</span>  <span style="color:#000000"> __Mongo__ </span>  <span style="color:#000000"> __D__ </span>  <span style="color:#000000"> __B__ </span>  <span style="color:#000000">to store images in same database as the metadata\.</span>

# eHermes Chooses Option 1

5\-5 How can eHermes benefit from a database system?

Use Microsoft SQL Server to store metadata\.

Less risky: uses known technology\.

Creates E\-R diagram\.

Decide to keep design simple at first\.

<img src="img/kroenke_emis9e_ppt_0516.jpg" width=500px />

# Nontraditional D B M S Products

5\-6 What are nontraditional DBMS products?

<span style="color:#000000"> __Relational model is not needed today__ </span>

<span style="color:#000000">Need to store new data types differently</span>

  * <span style="color:#000000"> __A__ </span>  <span style="color:#000000">tomic\,</span>  <span style="color:#000000"> __C__ </span>  <span style="color:#000000">onsistent\,</span>  <span style="color:#000000"> __I__ </span>  <span style="color:#000000">solated\,</span>  <span style="color:#000000"> __D__ </span>  <span style="color:#000000">urable transactions</span>
  * <span style="color:#000000">Critical to traditional commercial applications</span>
  * <span style="color:#000000">New Internet applications \(Twitter\) don’t need A</span>  <span style="color:#000000">C</span>  <span style="color:#000000">I</span>  <span style="color:#000000">D</span>
* <span style="color:#000000">NoSQL \(nonrelational\) DBMS</span>
  * <span style="color:#000000">DBMS products that support high transaction rates\, simple data structures\, replicated on many servers in the cloud\, without ACID transaction support\.</span>

# Need for Faster Processing Using Many Servers

* 5\-6 What are nontraditional DBMS products?
* <span style="color:#000000"> __Dynamo__ </span>
  * <span style="color:#000000">Amazon\-developed nonrelational data store</span>
* <span style="color:#000000"> __Bigtable__ </span>
  * <span style="color:#000000">Google\-developed nonrelational data store</span>
* <span style="color:#000000"> __Cassandra__ </span>
  * <span style="color:#000000">Facebook\-developed using concepts from both Dynamo and Bigtable</span>
* <span style="color:#000000"> __Top\-Level Project__ </span>  <span style="color:#000000">\(T</span>  <span style="color:#000000">L</span>  <span style="color:#000000">P\)</span>
  * <span style="color:#000000">Open\-source Cassandra by Apache</span>

# New Categories of D B M S

* 5\-6 What are nontraditional DBMS products?
* <span style="color:#000000"> __New__ </span>  <span style="color:#000000"> __S__ </span>  <span style="color:#000000"> __Q__ </span>  <span style="color:#000000"> __L D__ </span>  <span style="color:#000000"> __B__ </span>  <span style="color:#000000"> __M__ </span>  <span style="color:#000000"> __S__ </span>
  * <span style="color:#000000">Process very high levels of transactions\, like No</span>  <span style="color:#000000">S</span>  <span style="color:#000000">Q</span>  <span style="color:#000000">L D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S\, but provide A</span>  <span style="color:#000000">C</span>  <span style="color:#000000">I</span>  <span style="color:#000000">D support\.</span>
  * <span style="color:#000000">May or may not support relational model\.</span>
  * <span style="color:#000000">Current hotbed of development\.</span>
* <span style="color:#000000"> __In\-memory__ </span>  <span style="color:#000000"> __D__ </span>  <span style="color:#000000"> __B__ </span>  <span style="color:#000000"> __M__ </span>  <span style="color:#000000"> __S__ </span>  <span style="color:#000000"> __using S__ </span>  <span style="color:#000000"> __Q__ </span>  <span style="color:#000000"> __L extension__ </span>
  * <span style="color:#000000">S</span>  <span style="color:#000000">A</span>  <span style="color:#000000">P H</span>  <span style="color:#000000">A</span>  <span style="color:#000000">N</span>  <span style="color:#000000">A\, Tableau\.</span>
  * <span style="color:#000000">High volume A</span>  <span style="color:#000000">C</span>  <span style="color:#000000">I</span>  <span style="color:#000000">D transaction support with complex relational query processing\.</span>

# Will These New Products Replace the Relational Model?

* 5\-6 What are nontraditional DBMS products?
* <span style="color:#000000">Probably not\.</span>
  * <span style="color:#000000">Conversion enormously expensive and disruptive</span>
  * <span style="color:#000000">No</span>  <span style="color:#000000">S</span>  <span style="color:#000000">Q</span>  <span style="color:#000000">L D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S products very technical and require a deep background in computer science to use</span>
* <span style="color:#000000">No</span>  <span style="color:#000000">S</span>  <span style="color:#000000">Q</span>  <span style="color:#000000">L’s impact on D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S product market?</span>
  * <span style="color:#000000">Database software market experience viable new entrants</span>

# What Do Nonrelational DBMS Mean for You?

* 5\-6 What are nontraditional DBMS products?
* <span style="color:#000000">What do nonrelational D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S mean for you?</span>
  * <span style="color:#000000">Knowledge is useful—stay abreast of developments</span>
  * <span style="color:#000000">Watch nonrelational D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S product developments from an investor’s perspective</span>
  * <span style="color:#000000">New opportunities and career paths will develop around nonrelational databases</span>
  * <span style="color:#000000">Use knowledge to separate yourself from competition when it comes to job interviews</span>

# How does the knowledge in this chapter help you?

<span style="color:#000000">Understand purpose of a database and ways databases are processed</span>

<span style="color:#000000">Know about new categories of nontraditional D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S</span>

<span style="color:#000000">This knowledge will enable you to be an effective team member when your organization has needs like those at eHermes</span>

# Querying Inequality?

* <span style="color:#000000">Ethics Guide</span>
* <span style="color:#000000">Increasing value of cryptocurrency makes mining an attractive prospect for Richard’s boss Steve\.</span>
* <span style="color:#000000">Richard discovers a crypto\-mining program running on company servers\.</span>
  * <span style="color:#000000">Only runs at night and during off hours</span>
  * <span style="color:#000000">Probably will only increase electricity consumption</span>
* <span style="color:#000000">What would you do from a categorical imperative and utilitarian perspectives?</span>

# Data Engineer

* <span style="color:#000000">Career Guide</span>
* <span style="color:#000000">Kailey Smith at Haven</span>
* <span style="color:#000000">Q\. What attracted you to this field?</span>
* <span style="color:#000000">A\.</span>  <span style="color:#000000">“I've always enjoyed working with computers and figuring things out\, but after taking my first information systems course…I was sold\. This is a field that will be growing and expanding with new and exciting opportunities\. There are so many different areas to explore\, and you can definitely be paid pretty well\!”</span>
* <span style="color:#000000">Q\. What advice would you give to someone who is considering working in your field?</span>
* <span style="color:#000000">A\.</span>  <span style="color:#000000">“Keep an open mind\. Try out new things\. When I was in school\, I was focused on the security side of things because it sounded more exciting\, but I ended up working more on the data side\. Figure out what really excites you\, but the more you learn\, the more opportunities will open up to you\.”</span>

# Active Review

__5\-1__  <span style="color:#000000">Why do you need to know about databases?</span>

__5\-2__  <span style="color:#000000">What is a database?</span>

__5\-3__  <span style="color:#000000">What is a database management system \(D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S\)?</span>

__5\-4__  <span style="color:#000000">How do database applications make databases more useful?</span>

__5\-5__  <span style="color:#000000">How can eHermes benefit from a database system?</span>

__5\-6__  <span style="color:#000000">What are nontraditional D</span>  <span style="color:#000000">B</span>  <span style="color:#000000">M</span>  <span style="color:#000000">S products?</span>

# Dean’s Piano Database

<span style="color:#000000">Case Study 5</span>

<span style="color:#000000">Certified piano tuner and technician repairing and restoring pianos for many years\.</span>

<span style="color:#000000">Clown entertainer at children’s parties\.</span>

__Figure 5\-17__ Deano the Clown

<img src="img/kroenke_emis9e_ppt_0517.png" width=328px />

__Source__ : Dean Petrich

# Pianos in Storage

Case Study 5

__Figure 5\-18__ Pianos in Storage

__Figure 5\-19__ Pianos in Tent

<img src="img/kroenke_emis9e_ppt_0518.png" width=395px />

<img src="img/kroenke_emis9e_ppt_0519.png" width=500px />

__Source:__ David Kroenke

__Source__ :David Kroenke

# Columns in the Piano Table

Case Study 5

__Figure 5\-20__ Columns in the Piano Table

<img src="img/kroenke_emis9e_ppt_0520.jpg" width=500px />

# Query Design and Result

Case Study 5

<span style="color:#000000"> __Figure 5\-21__ </span>  <span style="color:#000000">Example of Access Query</span>

<img src="img/kroenke_emis9e_ppt_0521.jpg" width=500px />

<span style="color:#000000"> __Source__ </span>  <span style="color:#000000">: Microsoft Corporation</span>

# Results from Query

Case Study 5

<span style="color:#000000"> __Figure 5\-22__ </span>  <span style="color:#000000">Piano Sound Quality by Building</span>

<img src="img/kroenke_emis9e_ppt_0522.jpg" width=500px />

# Piano Sound Quality by Building

Case Study 5

__Figure 5\-23__ Results of Query from Figure 5\-21

<img src="img/kroenke_emis9e_ppt_0523.jpg" width=500px />

# Copyright

<img src="img/kroenke_emis9e_ppt_0524.png" width=500px />

