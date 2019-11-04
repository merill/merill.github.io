---
id: 535
title: ASP.NET StackOverflowException
date: 2003-07-24T21:00:56+00:00


guid: /post/2003/07/ASPNET-StackOverflowException.aspx
permalink: /2003/07/aspnet-stackoverflowexception/
dsq_thread_id:
  - "77713000"
categories:
  - ASP.NET
  - Technology
---
<body xmlns="http://www.w3.org/1999/xhtml">
    <p>
        What do you do when&#160;ASP.NET throws an exception like this? 
    </p>
    <h2><i>Exception of type System.StackOverflowException was thrown.</i> 
    </h2>
    <p>
        <font face="Arial, Helvetica, Geneva, SunSans-Regular, sans-serif "><b>Description: </b>An
        unhandled exception occurred during the execution of the current web request. Please
        review the stack trace for more information about the error and where it originated
        in the code. 
        <br />
        <br />
        <b>Exception Details: </b>System.StackOverflowException: Exception of type System.StackOverflowException
        was thrown.<br />
        <br />
        <b>Source Error:</b> 
        <br />
        <br />
        <table width="90%" bgcolor="#ffffcc">
            <tbody>
                <tr>
                    <td>
                        <code>An unhandled exception was generated during the execution of the current web
                        request. Information regarding the origin and location of the exception can be identified
                        using the exception stack trace below.</code> 
                    </td>
                </tr>
            </tbody>
        </table>
        <br />
        <b><font face="Verdana">Stack Trace:</font></b> 
        <br />
        <br />
        <table width="90%" bgcolor="#ffffcc">
            <tbody>
                <tr>
                    <td>
                        [StackOverflowException: Exception of type System.StackOverflowException was thrown.]
                        </td>
                </tr>
            </tbody>
        </table>
        <br />
        </font>
    </p>
    <hr width="90%" color="silver" size="1" />
    <p>
        <b><font face="Verdana">Version Information:</font></b>&#160;Microsoft .NET Framework
        Version:1.1.4322.573; ASP.NET Version:1.1.4322.573 
        <!-- 
[StackOverflowException]: Exception of type System.StackOverflowException was thrown.
[HttpUnhandledException]: Exception of type System.Web.HttpUnhandledException was thrown.
   at System.Web.UI.Page.HandleError(Exception e)
   at System.Web.UI.Page.ProcessRequestMain()
   at System.Web.UI.Page.ProcessRequest()
   at System.Web.UI.Page.ProcessRequest(HttpContext context)
   at System.Web.CallHandlerExecutionStep.System.Web.HttpApplication+IExecutionStep.Execute()
   at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)
-->
    </p>
</body>