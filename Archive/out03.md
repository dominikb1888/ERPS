# Experiencing M I S

Ninth Edition

<img src="img/kroenke_emis9e_ppt_030.jpg" width=500px />

__Chapter 3__

Business Intelligence Systems

Slides in this presentation contain hyperlinks\. JAWS users should be able to get a list of links by using INSERT\+F7

Copyright © 2021\, 2019\, 2017 Pearson Education\, Inc\. All Rights Reserved

# “Data analysis, where you don’t know the second question to ask until you see the answer to the first one.”

<span style="color:#000000">Having great success with grocery stores wanting to compete with online retailers like Walmart and Amazon</span>

<span style="color:#000000">Grocery stores are hesitant to share customer data</span>

<span style="color:#000000">Worried about customer privacy</span>

<span style="color:#000000">Use anonymized data with public data to identify customers? Data triangulation?</span>

<span style="color:#000000">Get data in spreadsheet to start</span>

<span style="color:#000000">Will need a data mart to combine all of the data</span>

# Study Questions

__3\-1__ How do organizations use business intelligence \(BI\) systems?

__3\-2__ What are the three primary activities in the BI process?

__3\-3__ How do organizations use data warehouses and data marts to acquire data?

__3\-4__ What are three techniques for processing BI data?

__3\-5__ What are the alternatives for publishing BI?

# Components of Business Intelligence (B I) Systems

3\-1 How do organizations use business intelligence \(BI\) systems?

<span style="color:#000000"> __Figure 3\-1__ </span>  <span style="color:#000000">Structure of a Business Intelligence System</span>

<img src="img/kroenke_emis9e_ppt_031.jpg" width=500px />

# How Do Organizations Use B I?

3\-1 How do organizations use business intelligence \(BI\) systems?

<span style="color:#000000"> __Figure 3\-2__ </span>  <span style="color:#000000">Example Uses of Business Intelligence</span>

<img src="img/kroenke_emis9e_ppt_032.jpg" width=500px />

# What are Typical Uses for B I?

* 3\-1 How do organizations use business intelligence \(BI\) systems?
* <span style="color:#000000">Identifying changes in purchasing patterns</span>
  * <span style="color:#000000">Important life events change what customers buy\.</span>
* <span style="color:#000000">Entertainment</span>
  * <span style="color:#000000">Netflix has data on watching\, listening\, and rental habits\.</span>
  * <span style="color:#000000">Classify customers by viewing patterns\.</span>

# Just-In-Time Medical Reporting

* 3\-1 How do organizations use business intelligence \(BI\) systems?
* <span style="color:#000000">Example of real time data mining and reporting\.</span>
* <span style="color:#000000">Injection notification services</span>
  * <span style="color:#000000">Software analyzes patient’s records\, if injections needed\, recommends as exam progresses\.</span>
* <span style="color:#000000">Blurry edge of medical ethics\.</span>

# Three Primary Activities in the B I Process

3\-2 What are the three primary activities in the BI process?

<span style="color:#000000"> __Figure 3\-3__ </span>  <span style="color:#000000">Three Primary Activities in the B</span>  <span style="color:#000000">I Process</span>

<img src="img/kroenke_emis9e_ppt_033.jpg" width=500px />

# Using Business Intelligence to Find Candidate Parts

* 3\-2 What are the three primary activities in the BI process?
* <span style="color:#000000">Identify parts that might qualify\.</span>
  * <span style="color:#000000">Provided by vendors who make part design files available for sale\.</span>
  * <span style="color:#000000">Purchased by larger customers\.</span>
  * <span style="color:#000000">Frequently ordered parts\.</span>
  * <span style="color:#000000">Ordered in small quantities\.</span>
* <span style="color:#000000">Used part weight and price surrogates for simplicity\.</span>

# Acquire Data: Extracted Order Data

* 3\-2 What are the three primary activities in the BI process?
* <span style="color:#000000">Query</span>
  * <span style="color:#000000"> _Sales_ </span>  <span style="color:#000000">\(CustomerName\, Contact\, Title\, Bill Year\, Number Orders\, Units\, Revenue\, Source\, PartNumber\)</span>
  * <span style="color:#000000"> _Part_ </span>  <span style="color:#000000">\(PartNumber\, Shipping Weight\, Vendor\)</span>

<span style="color:#000000"> __Figure 3\-4__ </span>  <span style="color:#000000">Sample Extracted Data: Order Extract Table and Part Data Table</span>

<img src="img/kroenke_emis9e_ppt_034.jpg" width=500px />

<span style="color:#000000"> __Source__ </span>  <span style="color:#000000">: Microsoft Corporation</span>

# Sample Extracted Data: Part Data Table

3\-2 What are the three primary activities in the BI process?

__Figure 3\-5__ Customer Summary

<img src="img/kroenke_emis9e_ppt_035.jpg" width=500px />

<span style="color:#000000"> __Source__ </span>  <span style="color:#000000">: Microsoft Corporation</span>

# Analyze Data

3\-2 What are the three primary activities in the BI process?

<span style="color:#000000"> __Figure 3\-6__ </span>  <span style="color:#000000">Qualifying Parts Query Results</span>

<img src="img/kroenke_emis9e_ppt_036.jpg" width=500px />

# Sample Orders and Parts View Data

3\-2 What are the three primary activities in the BI process?

__Figure 3\-7__ Sales History for Selected Parts

<img src="img/kroenke_emis9e_ppt_037.jpg" width=500px />

# Using Data Warehouses and Data Marts to Acquire Data

* 3\-3 How do organizations use data warehouses and data marts to acquire data?
* <span style="color:#000000">Functions of a data warehouse</span>
  * <span style="color:#000000">Obtain data from operational\, internal\, and external databases\.</span>
  * <span style="color:#000000">Cleanse data\.</span>
  * <span style="color:#000000">Organize and relate data\.</span>
  * <span style="color:#000000">Catalog data using metadata\.</span>

# Components of a Data Warehouse

3\-3 How do organizations use data warehouses and data marts to acquire data?

__Figure 3\-8__ Components of a Data Warehouse

<img src="img/kroenke_emis9e_ppt_038.jpg" width=500px />

# Examples of Consumer Data That Can Be Purchased

3\-3 How do organizations use data warehouses and data marts to acquire data?

__Figure 3\-9__ Examples of Consumer Data That Can Be Purchased

<img src="img/kroenke_emis9e_ppt_039.jpg" width=500px />

# Possible Problems with Operational Data

3\-3 How do organizations use data warehouses and data marts to acquire data?

__Figure 3\-10__ Possible Problems with Source Data

<img src="img/kroenke_emis9e_ppt_0310.jpg" width=500px />

# Data Warehouses Versus Data Marts

3\-3 How do organizations use data warehouses and data marts to acquire data?

__Figure 3\-11__ Data Mart Examples

<img src="img/kroenke_emis9e_ppt_0311.jpg" width=500px />

# Reporting Analysis

* 3\-4 What are three techniques for processing BI data?
* <span style="color:#000000">Process of sorting\, grouping\, summing\, filtering\, and formatting structured data</span>
* <span style="color:#000000"> __Structured__ </span>  <span style="color:#000000"> __data__ </span>
  * <span style="color:#000000">Data in rows and columns like tables</span>
* <span style="color:#000000"> __Exception__ </span>  <span style="color:#000000"> __reports__ </span>
  * <span style="color:#000000">Produced when something out of predefined bounds occurs</span>
* <span style="color:#000000">Printed and dynamic reports</span>

# Types of B I Analysis

3\-4 What are three techniques for processing BI data?

<span style="color:#000000"> __Figure 3\-12__ </span>  <span style="color:#000000">Three Types of B</span>  <span style="color:#000000">I Analysis</span>

<img src="img/kroenke_emis9e_ppt_0312.jpg" width=500px />

# Data Mining

3\-4 What are three techniques for processing BI data?

<span style="color:#000000">Application of statistical techniques to find patterns and relationships among data for classification and prediction</span>

<span style="color:#000000">Combined discipline of statistics\, mathematics\, artificial intelligence\, and machine learning</span>

# Source of Disciplines of Data Mining

3\-4 What are three techniques for processing BI data?

__Figure 3\-13__ Disciplines of Data Mining

<img src="img/kroenke_emis9e_ppt_0313.jpg" width=500px />

# Two Broad Categories of Data Mining

3\-4 What are three techniques for processing BI data?

<span style="color:#000000"> __Unsupervised__ </span>  <span style="color:#000000">procedures</span>

  * <span style="color:#000000">Does not start with a priori hypothesis or model</span>
  * <span style="color:#000000">Hypothesized model created afterward based on analytical results to explain patterns found</span>
    * <span style="color:#000000">Example: Cluster analysis</span>

# Supervised Data Mining

3\-4 What are three techniques for processing BI data?

<span style="color:#000000"> __Supervised__ </span>  <span style="color:#000000">data mining uses a priori model to compute outcome of model</span>

<span style="color:#000000">Prediction\, such as multiple linear regression</span>

<span style="color:#000000">Ex: CellPhoneWeekendMinutes</span>

<img src="img/kroenke_emis9e_ppt_0314.png" width=500px />

# Big Data

* 3\-4 What are three techniques for processing BI data?
* <span style="color:#000000">Huge volume</span>
  * <span style="color:#000000">Petabyte and larger</span>
* <span style="color:#000000">Rapid velocity</span>
  * <span style="color:#000000">Generated rapidly</span>
* <span style="color:#000000">Great variety</span>
  * <span style="color:#000000">Structured data\, free\-form text\, log files\, graphics\, audio\, and video</span>

# MapReduce Processing Summary

3\-4 What are three techniques for processing BI data?

__Figure 3\-14__ MapReduce Processing Summary

<img src="img/kroenke_emis9e_ppt_0315.jpg" width=500px />

# Google Trends on the Term Web 2.0

3\-4 What are three techniques for processing BI data?

<span style="color:#000000"> __Figure 3\-15__ </span>  <span style="color:#000000">Google Trends on the Terms Web 2\.0 and Hadoop</span>

<img src="img/kroenke_emis9e_ppt_0316.jpg" width=500px />

# Hadoop

* 3\-4 What are three techniques for processing BI data?
* <span style="color:#000000">Open\-source program supported by Apache Foundation</span>
* <span style="color:#000000">Manages thousands of computers</span>
* <span style="color:#000000">Implements</span>  <span style="color:#000000"> __MapReduce__ </span>  <span style="color:#000000">\(written in Java\)</span>
* <span style="color:#000000">Amazon\.com supports Hadoop as part of E</span>  <span style="color:#000000">C3 cloud offering</span>
* <span style="color:#000000"> __Pig__ </span>  <span style="color:#000000">query language platform for large dataset analysis</span>
  * <span style="color:#000000">Easy to master\, extensible\, and automatically optimizes queries on map\-reduce level</span>

# Geofencing for businesses?

<span style="color:#000000">So What?</span>

<span style="color:#000000">Geofencing is a location service that allows applications to know when a user has crossed a virtual fence \(specific location\)</span>

<span style="color:#000000">Crossing a fence can trigger an automated action</span>

<span style="color:#000000">Determine her location and identify local sales</span>

<span style="color:#000000">Supported by more than 90% of smartphones</span>

<span style="color:#000000">Used to send recruiting ads to qualified nurses who live in or frequent certain geofenced zones</span>

# Geofencing for businesses? (con’t)

<span style="color:#000000">So What?</span>

<span style="color:#000000">Is it becoming invasive and too much of a privacy concern?</span>

<span style="color:#000000">80% of people surveyed want to receive location\-based alerts from businesses</span>

<span style="color:#000000">Could geofencing be integrated with IoT devices to create an even more efficient smart home? How?</span>

<span style="color:#000000">How could a university leverage the benefits of geofencing on campus to improve student life and safety?</span>

# B I Publishing Alternatives

3\-5 What are the alternatives for publishing BI?

__Figure 3\-16__ BI Publishing Alternatives

<img src="img/kroenke_emis9e_ppt_0317.jpg" width=500px />

# What are the Two Functions of a B I Server?

3\-5 What are the alternatives for publishing BI?

<span style="color:#000000">Management and delivery</span>

__Figure 3\-17__ Components of a Generic Business Intelligence System

<img src="img/kroenke_emis9e_ppt_0318.jpg" width=500px />

# How Does the Knowledge in This Chapter Help You?

<span style="color:#000000">Business intelligence a critical skill for future business professionals</span>

<span style="color:#000000">Business leaders prioritize the digital transformation of their businesses</span>

<span style="color:#000000">Business intelligence is a key technology supporting such digital transformation</span>

<span style="color:#000000">You now have a basic understanding of this increasingly important business discipline</span>

<span style="color:#000000">You can contribute by imagining possible uses of the data your organization generates</span>

# M I S-Diagnosis (1 of 2)

* <span style="color:#000000">Ethics Guide</span>
* <span style="color:#000000">Doctors are relying more and more on artificial intelligence \(A</span>  <span style="color:#000000">I\)\-driven expert systems to select the most appropriate medications and treatments\.</span>
* <span style="color:#000000">Ordered to improve the system’s “perception” of the company’s drugs\.</span>
* <span style="color:#000000">Minor modifications to the drug’s profile made a big difference\.</span>
  * <span style="color:#000000">But some of the numbers he used to modify the profile were</span>  <span style="color:#000000"> __not__ </span>  <span style="color:#000000">accurate\.</span>
  * <span style="color:#000000">The changes would warrant a</span>  <span style="color:#000000"> __regulatory review__ </span>  <span style="color:#000000">\.</span>

Ethics Guide

<span style="color:#000000">Suppose the company alters the drug profile\.</span>

<span style="color:#000000">Would the company be liable if something happened to a patient who took the drug based on</span>  <span style="color:#000000"> __altered__ </span>  <span style="color:#000000">information?</span>

<span style="color:#000000">Do you think that manipulating the recommendation of an A</span>  <span style="color:#000000">I system even though the new recommendation may be for the better drug is ethical according to the categorical imperative\, and utilitarian perspective?</span>

# Manager, Data and Analytics

* <span style="color:#000000">Career Guide</span>
* <span style="color:#000000">Lindsey Tsuya at Nike Inc\.</span>
  * <span style="color:#000000">Q\. What attracted you to this field?</span>
    * <span style="color:#000000">A\. “As a college student\, I worked in the service industry\. When I was selecting my degree\, I knew I wanted two things\. First\, I wanted a degree that made money\. Second\, I wanted a job that did not involve direct provision of service to the public\. By choosing information systems\, I knew I would be doing more of a behind\-the\-scenes job\.”</span>
  * <span style="color:#000000">Q\. What advice would you give to someone who is considering working in your field?</span>
    * <span style="color:#000000">A\. “No matter what field you choose\, make sure it is something you are passionate about because if you are not passionate about it\, work will feel like…work\.”</span>

# Active Review

__3\-1__  <span style="color:#000000">How do organizations use business intelligence \(B</span>  <span style="color:#000000">I\) systems?</span>

__3\-2__  <span style="color:#000000">What are the three primary activities in the B</span>  <span style="color:#000000">I process?</span>

__3\-3__  <span style="color:#000000">How do organizations use data warehouses and data marts to acquire data?</span>

__3\-4__  <span style="color:#000000">What are three techniques for processing B</span>  <span style="color:#000000">I data?</span>

__3\-5__  <span style="color:#000000">What are the alternatives for publishing B</span>  <span style="color:#000000">I?</span>

# Hadoop the Cookie Cutter (1 of 2)

* <span style="color:#000000">Case Study 3</span>
* <span style="color:#000000">Third\-party cookie created by site other than one you visited\.</span>
* <span style="color:#000000">Most commonly occurs when a Web page includes content from multiple sources\.</span>
* <span style="color:#000000">[DoubleClick](https://www.doubleclickbygoogle.com/)</span>
  * <span style="color:#000000">I</span>  <span style="color:#000000">P address where content was delivered\.</span>
    * <span style="color:#000000">DoubleClick instructs your browser to store a DoubleClick cookie\.</span>
  * <span style="color:#000000">Records data in cookie log on DoubleClick’s server\.</span>

Case Study 3

<span style="color:#000000">Third\-party cookie owner has history of what was shown\, what ads you clicked\, and intervals between interactions\.</span>

<span style="color:#000000">Cookie log shows how you respond to ads and your pattern of visiting various Web sites where ads placed\.</span>

<span style="color:#000000">[Firefox Lightbeam](https://addons.mozilla.org/en-us/firefox/addon/lightbeam/reviews/)</span>  <span style="color:#000000">tracks and graphs cookies on your computer\.</span>

# Firefox Lightbeam: Display on Start up

Case Study 3

<span style="color:#000000">No cookies on startup\.</span>

<span style="color:#000000"> __Figure 3\-18a__ </span>  <span style="color:#000000">Third\-Party Cookie Growth</span>

<img src="img/kroenke_emis9e_ppt_0319.jpg" width=500px />

<span style="color:#000000"> __Source__ </span>  <span style="color:#000000">: © Mozilla Corporation</span>

# After Visiting M S N.com

Case Study 3

<span style="color:#000000">After</span>  <span style="color:#000000">[M](https://www.msn.com/en-in/)</span>  <span style="color:#000000">[S](https://www.msn.com/en-in/)</span>  <span style="color:#000000">[N\.com](https://www.msn.com/en-in/)</span>  <span style="color:#000000">and Gmail\.</span>

<span style="color:#000000"> __Figure 3\-18b__ </span>  <span style="color:#000000">Third\-Party Cookie Growth</span>

<img src="img/kroenke_emis9e_ppt_0320.jpg" width=500px />

<span style="color:#000000"> __Source:__ </span>  <span style="color:#000000">© Mozilla Corporation</span>

# 5 Sites Visited Yields 27 Third Parties

Case Study 3

<span style="color:#000000">Five sites visited yield 27 third parties\.</span>

<span style="color:#000000"> __Figure 3\-18c__ </span>  <span style="color:#000000">Third\-Party Cookie Growth</span>

<img src="img/kroenke_emis9e_ppt_0321.jpg" width=500px />

<span style="color:#000000"> __Source:__ </span>  <span style="color:#000000">© Mozilla Corporation</span>

# Sites Connected to Doubleclick

Case Study 3

<span style="color:#000000">Sites connected to DoubleClick\.</span>

<span style="color:#000000"> __Figure 3\-18d__ </span>  <span style="color:#000000">Third\-Party Cookie Growth</span>

<img src="img/kroenke_emis9e_ppt_0322.jpg" width=500px />

<span style="color:#000000"> __Source:__ </span>  <span style="color:#000000">© Mozilla Corporation</span>

# Copyright

<img src="img/kroenke_emis9e_ppt_0323.png" width=500px />

