---
id: 351
title: 'ASP.NET 2.0: DataGrid Sample'
date: 2004-02-11T14:22:35+00:00
author: Merill Fernando
layout: post
guid: /post/2004/02/ASPNET-20-DataGrid-Sample.aspx
permalink: /2004/02/aspnet-20-datagrid-sample/
dsq_thread_id:
  - "80577373"
categories:
  - .NET
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <div class="Section1">
        <p class="MsoNormal">
            ASP.NET 2.0 streamlines data-driven application development. This example uses the
            categories and product tables in SQL Server's Northwind sample database, displaying
            the categories in a dropdown list. This code listing uses the selected category in
            the dropdown list to display all the products in that category in a GridView control.
        </p>
        <p class="MsoNormal" style='text-autospace:none'>
            <span style=';font-family:"Courier New";background:yellow'>&lt;%@ page language="C#"
            %&gt;<br />
            </span><font color="blue"><span style=';font-family:"Courier New";color:blue'>&lt;</span></font><font color="maroon"><span style='; font-family:"Courier New";color:maroon'>html</span></font><span style=';font-family:"Courier New"; color:blue'>&gt;<br />
            &lt;</span><font color="maroon"><span style=';font-family:"Courier New";color:maroon'>head</span></font><font color="red"><span style=';font-family:"Courier New"; color:red'>runat</span></font><font color="blue"><span style=';font-family:"Courier New";color:blue'>="server"</span></font><font color="red"><span style=';font-family:"Courier New"; color:red'>ID</span></font><font color="blue"><span style=';font-family:"Courier New";color:blue'>="Head1"</span></font><font color="red"><span style=';font-family:"Courier New"; color:red'>NAME</span></font><font color="blue"><span style=';font-family:"Courier New";color:blue'>="Head1"&gt;<br />
            </span></font><span style='; font-family:"Courier New"'>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;</span></font><font color="maroon"><span style='color:maroon'>title</span></font><font color="blue"><span style='color:blue'>&gt;</span></font>SqlDataSource<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Example<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;/</span></font><font color="maroon"><span style='color:maroon'>title</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            &lt;/</span></font><font color="maroon"><span style='color:maroon'>head</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            &lt;</span></font><font color="maroon"><span style='color:maroon'>body</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            &lt;</span></font><font color="maroon"><span style='color:maroon'>form</span></font><font color="red"><span style='color:red'>runat</span></font><font color="blue"><span style='color:blue'>="server"</span></font><font color="red"><span style='color:red'>ID</span></font><font color="blue"><span style='color:blue'>="Form1"&gt;</span></font>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;<br />
            &#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;</span></font><font color="maroon"><span style='color:maroon'>asp:sqldatasource</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>id</span></font><font color="blue"><span style='color:blue'>="categoriesDataSource"</span></font><font color="fuchsia"><span style='color:fuchsia'>&#160;&#160;&#160;&#160;<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>runat</span></font><font color="blue"><span style='color:blue'>="server"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>datasourcemode</span></font><font color="blue"><span style='color:blue'>="DataSet"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>connectionstring</span></font><font color="blue"><span style='color:blue'>="Data<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Source=localhost;uid=sa;<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; pwd=;Initial<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Catalog=Northwind;"<br />
            </span></font><font color="fuchsia"><span style='color:fuchsia'>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>selectcommand</span></font><font color="blue"><span style='color:blue'>="usp_GetCategories"&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;/</span></font><font color="maroon"><span style='color:maroon'>asp:sqldatasource</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160; Select Categories:<br />
            &#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;</span></font><font color="maroon"><span style='color:maroon'>asp:dropdownlist</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>id</span></font><font color="blue"><span style='color:blue'>="ddlCategoriesList"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>runat</span></font><font color="blue"><span style='color:blue'>="server"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>datavaluefield</span></font><font color="blue"><span style='color:blue'>="CategoryID"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>datasourceid</span></font><font color="blue"><span style='color:blue'>="categoriesDataSource"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>autopostback</span></font><font color="blue"><span style='color:blue'>="true"<br />
            </span></font><font color="fuchsia"><span style='color:fuchsia'>&#160;&#160;&#160;&#160;&#160;
            &#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>datatextfield</span></font><font color="blue"><span style='color:blue'>="CategoryName"&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;/</span></font><font color="maroon"><span style='color:maroon'>asp:dropdownlist</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;</span></font><font color="maroon"><span style='color: maroon'>asp:sqldatasource</span></font><font color="red"><span style='color:red'>runat</span></font><font color="blue"><span style='color:blue'>="server"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>id</span></font><font color="blue"><span style='color:blue'>="productsDataSource"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>datasourcemode</span></font><font color="blue"><span style='color:blue'>="DataReader"<br />
            </span></font><font color="fuchsia"><span style='color:fuchsia'>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>connectionstring</span></font><font color="blue"><span style='color:blue'>="Data<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Source=localhost;uid=sa;pwd=;<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Initial Catalog=Northwind;"<br />
            </span></font><font color="fuchsia"><span style='color:fuchsia'>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>selectcommand</span></font><font color="blue"><span style='color:blue'>="SELECT
            ProductID,<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; ProductName, QuantityPerUnit,<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; UnitPrice&#160;
            FROM Products Where<br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; CategoryID=@CategoryID"&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;</span></font><font color="maroon"><span style='color:maroon'>selectparameters</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;</span></font><font color="maroon"><span style='color:maroon'>asp:controlparameter</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>defaultvalue</span></font><font color="blue"><span style='color:blue'>="1"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>name</span></font><font color="blue"><span style='color:blue'>="CategoryID"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>propertyname</span></font><font color="blue"><span style='color:blue'>="SelectedValue"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>controlid</span></font><font color="blue"><span style='color:blue'>="ddlCategoriesList"&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;/</span></font><font color="maroon"><span style='color:maroon'>asp:controlparameter</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;/</span></font><font color="maroon"><span style='color:maroon'>selectparameters</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;/</span></font><font color="maroon"><span style='color:maroon'>asp:sqldatasource</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;</span></font><font color="maroon"><span style='color: maroon'>br</span></font><font color="blue"><span style='color:blue'>/&gt;&lt;</span></font><font color="maroon"><span style='color:maroon'>b</span></font><font color="blue"><span style='color:blue'>&gt;&lt;</span></font><font color="maroon"><span style='color:maroon'>br</span></font><font color="blue"><span style='color:blue'>/&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160; Product Details<font color="blue"><span style='color:blue'>&lt;</span></font><font color="maroon"><span style='color: maroon'>br</span></font><font color="blue"><span style='color:blue'>/&gt;&lt;/</span></font><font color="maroon"><span style='color:maroon'>b</span></font><font color="blue"><span style='color:blue'>&gt;&lt;</span></font><font color="maroon"><span style='color:maroon'>br</span></font><font color="blue"><span style='color:blue'>/&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;</span></font><font color="maroon"><span style='color: maroon'>asp:gridview</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>id</span></font><font color="blue"><span style='color:blue'>="productsGrid"</span></font><font color="red"><span style='color:red'>runat</span></font><font color="blue"><span style='color:blue'>="server"</span></font><font color="fuchsia"><span style='color:fuchsia'>
            <br />
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span></font> <font color="red"><span style='color:red'>datasourceid</span></font><font color="blue"><span style='color:blue'>="productsDataSource"&gt;<br />
            </span></font>&#160;&#160;&#160;&#160;&#160; <font color="blue"><span style='color:blue'>&lt;/</span></font><font color="maroon"><span style='color:maroon'>asp:gridview</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            &lt;/</span></font><font color="maroon"><span style='color:maroon'>form</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            &lt;/</span></font><font color="maroon"><span style='color:maroon'>body</span></font><font color="blue"><span style='color:blue'>&gt;<br />
            &lt;/</span></font><font color="maroon"><span style='color:maroon'>html</span></font><font color="blue"><span style='color:blue'>&gt;</span></font></span>
        </p>
    </div>
</body>