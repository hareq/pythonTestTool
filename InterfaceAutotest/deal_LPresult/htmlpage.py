# -*- coding:utf-8 -*-
__author__ = 'guyh'
import os,sys

html = open('index.html', 'w')
html.write(r"""
<html class="splitter-invoked" autopagermatchedrules="1"><head>
    <title>diy_1线程与10线程 - 搜索产品研发部 - Confluence</title>








    <meta http-equiv="X-UA-Compatible" content="IE=EDGE,chrome=IE7">
<meta charset="UTF-8">
<!-- Deprecated since 3.4. To be removed in a future version of Confluence; use AJS.Confluence.getContextPath() -->
<meta id="confluence-context-path" name="confluence-context-path" content="">
<meta id="confluence-base-url" name="confluence-base-url" content="http://conf.ctripcorp.com">

<meta id="atlassian-token" name="atlassian-token" content="dfffda9cbc483e2c91bf2838d86b794acc8de2da">

<meta id="confluence-space-key" name="confluence-space-key" content="SPD">
<script async="" src="//www.google-analytics.com/analytics.js"></script><script async="" src="//www.google-analytics.com/analytics.js"></script><script type="text/javascript">
    // Deprecated global variables. To be removed in a future version of Confluence.
    var contextPath = '';
</script>



<!-- include system css resources -->


    <!--[if lt IE 9]>
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/140/_/download/superbatch/css/batch.css?conditionalComment=lt+IE+9" media="all">
<![endif]-->
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/140/_/download/superbatch/css/batch.css?media=print" media="print">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/140/_/download/superbatch/css/batch.css" media="all">
<!--[if gte IE 9]>
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/140/_/download/superbatch/css/batch.css?conditionalComment=gte+IE+9" media="all">
<![endif]-->
<!--[if lte IE 8]>
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/140/_/download/superbatch/css/batch.css?conditionalComment=lte+IE+8" media="all">
<![endif]-->
<!--[if lte IE 9]>
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/140/_/download/superbatch/css/batch.css?conditionalComment=lte+IE+9" media="all">
<![endif]-->
<!--[if lt IE 9]>
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/0331592c94a9984f2e20d08266ef5287/_/download/contextbatch/css/page/batch.css?conditionalComment=lt+IE+9" media="all">
<![endif]-->
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/0331592c94a9984f2e20d08266ef5287/_/download/contextbatch/css/page/batch.css" media="all">
<!--[if lt IE 9]>
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/c7b2e49c8b2afffb10df68f5a47a2454/_/download/contextbatch/css/viewcontent/batch.css?conditionalComment=lt+IE+9" media="all">
<![endif]-->
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/c7b2e49c8b2afffb10df68f5a47a2454/_/download/contextbatch/css/viewcontent/batch.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/98a119ae206d65814c97a587147e27d2/_/download/contextbatch/css/plugin.quick.comment.pre/batch.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/87ad8563151abba0fae763c91f899eea/_/download/contextbatch/css/main/batch.css" media="all">
<!--[if lt IE 9]>
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/8c811a9f7080494419b51d8385e5cfb8/_/download/contextbatch/css/atl.general/batch.css?conditionalComment=lt+IE+9" media="all">
<![endif]-->
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/8c811a9f7080494419b51d8385e5cfb8/_/download/contextbatch/css/atl.general/batch.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2.1.5/_/download/batch/com.atlassian.confluence.plugins.pagetree:pagetree-resources/com.atlassian.confluence.plugins.pagetree:pagetree-resources.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2.1.5/_/download/batch/com.atlassian.confluence.plugins.pagetree:pagetree-pdg-resources/com.atlassian.confluence.plugins.pagetree:pagetree-pdg-resources.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/1.1.22/_/download/batch/com.atlassian.mywork.mywork-confluence-host-plugin:mw-header-anchor/com.atlassian.mywork.mywork-confluence-host-plugin:mw-header-anchor.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/1/_/styles/colors.css?spaceKey=SPD" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_/download/resources/com.atlassian.confluence.plugins.doctheme:documentation/default-theme.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_/download/resources/com.atlassian.confluence.plugins.doctheme:documentation/doc-theme.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_/download/resources/com.atlassian.confluence.plugins.doctheme:documentation/splitter.css" media="all">

<!-- end system css resources -->

    <meta name="confluence-request-time" content="1434615569363">
<!-- Deprecated since 3.4. To be removed in a future version of Confluence; use atl.header -->

            <script type="text/x-template" title="share-content-popup">
    <form action="#" method="post" class="aui share-content-popup">
        <div class="field-group">
            <div class="autocomplete-user-target">
                <input class="text autocomplete-sharepage" id="users" data-max="10" data-dropdown-target=".autocomplete-user-target" data-none-message="No matching user or email found" placeholder="User name or email"/>
            </div>
            <ol class="recipients">
            </ol>
        </div>
        <div class="field-group">
            <textarea class="textarea" id="note" placeholder="Add an optional note"/>
        </div>
        <div class="field-group button-panel">
            <div class="progress-messages-icon"></div>
            <div class="progress-messages">
            </div>
            <input class="button submit" type="submit" value="Share" disabled/>
            <a class="close-dialog" href="#">Cancel</a>
        </div>
    </form>
</script>

<script type="text/x-template" title="share-content-popup-recipient-username">
    <li data-username="{username}" style="display: none">
        <span>
            <img src="{thumbnailLink.href}" title="{title}">
            <span>{title}</span>
            <span class="remove-recipient"/>
        </span>
    </li>
</script>

<script type="text/x-template" title="share-content-popup-recipient-email">
    <li data-email="{email}" style="display: none">
        <span>
            <img src="{icon}" title="{email}">
            <span>{email}</span>
            <span class="remove-recipient"/>
        </span>
    </li>
</script>


            <meta name="ajs-use-keyboard-shortcuts" content="true">
            <meta name="ajs-keyboardshortcut-hash" content="23dffa48548c291ac6affe9b07b7cd83">
            <meta name="ap-request-id" content="2e101210b9e07de6">
            <style>.ia-fixed-sidebar, .ia-splitter-left {width: 285px;}.theme-default .ia-splitter #main {margin-left: 285px;}.acs-side-bar {visibility: hidden;}</style>






            <meta name="ajs-page-id" content="58582949">
            <meta name="ajs-content-type" content="page">
            <meta name="ajs-page-title" content="diy_1线程与10线程">
            <meta name="ajs-parent-page-title" content="【Diy】">
            <meta name="ajs-parent-page-id" content="58582307">
            <meta name="ajs-space-key" content="SPD">
            <meta name="ajs-space-name" content="搜索产品研发部">
            <meta name="ajs-from-page-title" content="">
            <meta name="ajs-user-display-name" content="gyh顾艳华">
            <meta name="ajs-editor.loader.comment.resources" content="<link type=&quot;text/css&quot; rel=&quot;stylesheet&quot; href=&quot;/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/3b60fb45fb287266a363724cfc45c0a0/_/download/contextbatch/css/comment-editor/batch.css&quot; media=&quot;all&quot;>
">
            <meta name="ajs-context-path" content="">
            <meta name="ajs-base-url" content="http://conf.ctripcorp.com">
            <meta name="ajs-version-number" content="5.1.2">
            <meta name="ajs-build-number" content="4224">
            <meta name="ajs-remote-user" content="guyh">
            <meta name="ajs-static-resource-url-prefix" content="/s/zh_CN-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/_">
            <meta name="ajs-global-settings-attachment-max-size" content="104857600">
            <meta name="ajs-user-locale" content="en_GB">
            <meta name="ajs-enabled-dark-features" content="">
            <meta name="ajs-atl-token" content="dfffda9cbc483e2c91bf2838d86b794acc8de2da">
            <meta name="ajs-confluence-flavour" content="VANILLA">
            <meta name="ajs-editor.loader.resources" content="<!--[if lt IE 9]>
<link type=&quot;text/css&quot; rel=&quot;stylesheet&quot; href=&quot;/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2a7bff19c04f45faa7841e765729b4f5/_/download/contextbatch/css/editor,macro-browser,fullpage-editor,-viewcontent/batch.css?conditionalComment=lt+IE+9&quot; media=&quot;all&quot;>
<![endif]-->
<link type=&quot;text/css&quot; rel=&quot;stylesheet&quot; href=&quot;/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2a7bff19c04f45faa7841e765729b4f5/_/download/contextbatch/css/editor,macro-browser,fullpage-editor,-viewcontent/batch.css&quot; media=&quot;all&quot;>
<link type=&quot;text/css&quot; rel=&quot;stylesheet&quot; href=&quot;/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2a7bff19c04f45faa7841e765729b4f5/_/download/contextbatch/css/editor,macro-browser,fullpage-editor,-viewcontent/batch.css?media=%28max-width%3A+1270px%29&quot; media=&quot;(max-width: 1270px)&quot;>
<script type=&quot;text/javascript&quot; src=&quot;/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2a7bff19c04f45faa7841e765729b4f5/_/download/contextbatch/js/editor,macro-browser,fullpage-editor,-viewcontent/batch.js&quot; ></script>
">
            <meta name="ajs-date.format" content="MMM dd, yyyy">

    <link rel="shortcut icon" href="/favicon.ico">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">

<link rel="search" type="application/opensearchdescription+xml" href="/opensearch/osd.action" title="Confluence">

    <!-- include system javascript resources -->
    <script type="text/javascript" src="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/140/_/download/superbatch/js/batch.js"></script>
<!--[if lte IE 8]>
<script type="text/javascript" src="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/140/_/download/superbatch/js/batch.js?conditionalComment=lte+IE+8" ></script>
<![endif]-->
<script type="text/javascript" src="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/0331592c94a9984f2e20d08266ef5287/_/download/contextbatch/js/page/batch.js"></script>
<script type="text/javascript" src="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/7a695ac574a6c906c9e9793319a39241/_/download/contextbatch/js/viewcontent,main,plugin.quick.comment.pre,atl.general/batch.js"></script>
<script type="text/javascript" src="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/95c8bb80f00f50c9163e243a8f23937e/_/download/contextbatch/js/atl.comments/batch.js"></script>
<script type="text/javascript" src="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2.1.5/_/download/batch/com.atlassian.confluence.plugins.pagetree:pagetree-resources/com.atlassian.confluence.plugins.pagetree:pagetree-resources.js"></script>
<script type="text/javascript" src="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/1.1.22/_/download/batch/com.atlassian.mywork.mywork-confluence-host-plugin:mw-header-anchor/com.atlassian.mywork.mywork-confluence-host-plugin:mw-header-anchor.js"></script>




    <!-- end system javascript resources -->
    <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-48540836-3', 'ctripcorp.com',{'siteSpeedSampleRate': 100});
  ga('send', 'pageview');

</script>


                <link rel="canonical" href="http://conf.ctripcorp.com/pages/viewpage.action?pageId=58582949">
        <link rel="shortlink" href="http://conf.ctripcorp.com/x/ped9Aw">
    <meta name="wikilink" content="[SPD:diy_1线程与10线程]">
    <meta name="page-version" content="1">

<!--[if lt IE 9]>
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2a7bff19c04f45faa7841e765729b4f5/_/download/contextbatch/css/editor,macro-browser,fullpage-editor,-viewcontent/batch.css?conditionalComment=lt+IE+9" media="all">
<![endif]--><link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2a7bff19c04f45faa7841e765729b4f5/_/download/contextbatch/css/editor,macro-browser,fullpage-editor,-viewcontent/batch.css" media="all"><link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2a7bff19c04f45faa7841e765729b4f5/_/download/contextbatch/css/editor,macro-browser,fullpage-editor,-viewcontent/batch.css?media=%28max-width%3A+1270px%29" media="(max-width: 1270px)">
            <meta name="ajs-content-type" content="page">
            <meta name="ajs-min-editor-height" content="150">
            <meta name="ajs-editor-plugin-resource-prefix" content="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_">
            <meta name="ajs-num-attachments" content="8">
            <meta name="ajs-auto-start" content="false">
            <meta name="ajs-cancel-button-close-text" content="Close">
            <meta name="ajs-content-id" content="58582949">
            <meta name="ajs-action-locale" content="en_GB">
            <meta name="ajs-save-drafts" content="true">
            <meta name="ajs-use-inline-tasks" content="true">
            <meta name="ajs-heartbeat" content="true">
            <meta name="ajs-cancel-button-discard-text" content="">
            <meta name="ajs-draft-id" content="0">
            <meta name="ajs-new-page" content="false">
            <meta name="ajs-form-name" content="inlinecommentform">
            <meta name="ajs-attachment-source-content-id" content="58582949">
            <meta name="ajs-editor-mode" content="richtext">
            <meta name="ajs-draft-type" content="page">
            <meta name="ajs-existing-draft-id" content="0">
            <meta name="ajs-can-attach-files" content="true">

            		    <meta name="ajs-max-thumb-width" content="300">
		    <meta name="ajs-can-send-email" content="true">
		    <meta name="ajs-is-dev-mode" content="false">
		    <meta name="ajs-draft-save-interval" content="30000">
		    <meta name="ajs-show-hidden-user-macros" content="false">
		    <meta name="ajs-is-admin" content="false">
		    <meta name="ajs-confluence.prefs.editor.disable.autocomplete" content="false">
		    <meta name="ajs-confluence.prefs.editor.disable.autoformat" content="false">
		    <meta name="ajs-heartbeat-interval" content="30000">

    </head>

<body onload="placeFocus()" id="com-atlassian-confluence" class="theme-documentation  aui-theme-default aui-layout splitter-invoked">


    <div id="full-height-container">
    <div id="header-precursor">

                    </div>






<header id="header" role="banner">
    <nav class="aui-header aui-dropdown2-trigger-group" role="navigation"><div class="aui-header-inner"><div class="aui-header-before"><a class="aui-dropdown2-trigger test-switcher-trigger" aria-owns="test-switcher" aria-haspopup="true" tabindex="0"></a><div id="test-switcher" class="aui-dropdown2 aui-style-default"></div><script>
            (function (NL) {
                var initialise = function () {
                    // For some milestones of AUI, the atlassian soy namespace was renamed to aui. Handle that here by ensuring that window.atlassian is defined.
                    window.atlassian = window.atlassian || window.aui;
                    new NL.AppSwitcher({
                        dropdownContents: '#test-switcher'
                    });
                };
                if (NL.AppSwitcher) {
                    initialise();
                } else {
                    NL.onInit = initialise;
                }
            }(window.NL = (window.NL || {})));
            window.NL.isUserAdmin = false</script></div></div><!-- .aui-header-inner--></nav><!-- .aui-header -->
    <br class="clear">
</header>

    <div id="splitter" style="position: relative; height: 300px;">
    <div class="vsplitbar" unselectable="on" style="z-index: 4; position: absolute; -webkit-user-select: none; cursor: ew-resize; left: 300px; height: 300px;"><a href="javascript:void(0)" accesskey="L" tabindex="0" title="vsplitbar"></a></div>
    <div id="splitter-content" style="position: absolute; left: 305px; width: 975px; height: 300px;">

                    <script type="text/javascript" src="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_/download/resources/com.atlassian.confluence.plugins.doctheme:resources/doc-theme.js"></script>



<div id="main" class="aui-page-panel">








































<div id="content" class="page view">


<div id="action-messages">
                        </div>




<script type="text/x-template" title="movePageDialog">
    <div class="row information">
        <div class="inner">
            <div class="element">
                Specify the new parent page for this page and its children by space and title.
            </div>
        </div>
    </div>
        <form class="aui" onsubmit="return false;">
	        <fieldset>


    <legend class="assistive"><span>Change the Parent Page to a Known Page</span></legend>
	            <div class="field-group">
	                <label for="new-space">New space:</label>
	                <div class="value new-space-value">
	                    <input id="new-space-key" name="new-space-key" type="hidden" value="SPD">
	                    	                        <span class="space-input">
	                            <input id="new-space" name="new-space" value="搜索产品研发部" disabled="disabled" class="text long-field">
	                        </span>
                            <div class="description warning">You cannot move this page to another space because you do not have permission to remove it from this space.</div>
	                    	                    <div class="new-space-dropdown aui-dd-parent autocomplete"></div>
	                </div>
	            </div>
	            <div class="field-group">
	                <label for="new-parent-page">New parent page:</label>
	                <div class="value new-parent-page-value">
	                    <span class="page-input">
	                        <input id="new-parent-page" name="new-parent-page" value="【Diy】" class="text long-field">
	                    </span>
                        <div class="description">Start typing a page title to see a list of suggestions.</div>
	                    <div class="new-parent-page-dropdown aui-dd-parent autocomplete"></div>
	                </div>
	            </div>
	        </fieldset>
        </form>
    <div class="location-info">
        <div class="row">
            <label>Current location:</label>
            <div class="value breadcrumbs-container">
                <div class="breadcrumbs-line">
                    <ul id="current-parent-breadcrumbs" class="breadcrumbs">
                    </ul>
                </div>
            </div>
        </div>
        <div class="row">
            <label>New location:</label>
            <div class="value breadcrumbs-container">
                <div class="breadcrumbs-line">
                    <ul id="new-parent-breadcrumbs" class="breadcrumbs">
                    </ul>
                </div>
            </div>
        </div>
    </div>
</script>

<script type="text/x-template" title="movePageSearchPanel">
    <div class="row information">
        <div class="inner">
            <div class="element">
                Search for and select the new parent page for this page and its children.
            </div>
        </div>
    </div>
    <div id="move-page-search-container" class="row">
	        <form class="aui" onsubmit="return false;">
	            <fieldset>


    <legend class="assistive"><span>Search for a New Parent Page</span></legend>


    <label  for="move-page-search-query" class="assistive">Search keywords</label>
	                <input class="search-query text" id="move-page-search-query">


    <label  for="move-page-search-space" class="assistive">Search in space</label>
	                	                    <select id="move-page-search-space" class="search-space select" disabled="disabled">
	                        <option value="SPD" selected="selected">搜索产品研发部</option>
	                    </select>
	                	                <input type="button" value="Search" class="button submit">
	                	                    <div class="description warning">You cannot move this page to another space because you do not have permission to remove it from this space.</div>
	                	            </fieldset>
	        </form>
        <div class="search-results">
        </div>
    </div>
</script>
<script type="text/x-template" title="searchResultsGrid">
    <table class="aui">
        <thead>
            <tr class="header">
                <th class="search-result-title">Page Title</th>
                <th class="search-result-space">Space</th>
                <th class="search-result-date">Updated</th>
            </tr>
        </thead>
    </table>
</script>
<script type="text/x-template" title="searchResultsGridCount">
    <p class="search-result-count">{0}</p>
</script>
<script type="text/x-template" title="searchResultsGridRow">
    <tr class="search-result">
        <th class="search-result-title"><a href="{1}" class="content-type-{2}"><span>{0}</span></a></th>
        <td class="search-result-space"><a class="space" href="/display/{4}/" title="{3}">{3}</a></td>
        <td class="search-result-date"><span class="date" title="{6}">{5}</span></td>
    </tr>
</script><!-- Start restrictions section -->
<script type="text/x-template" title="page-permissions-div">
<div id="page-permissions-div">
    <div id="page-permissions-editor-form">
                <div id="page-permissions-error-div" class="aui-message warning shadowed closeable hidden">
            <p class="title"/>
            <span class="aui-icon icon-warning"></span>
            <span class="aui-icon icon-close" tabindex="0" role="button"></span>
        </div>
                <div id="page-permissions-type-radios" class="page-permissions-label-rows">
            <div class="radio">
                <input id="restrictViewRadio" class="radio" type="radio" checked="checked" name="pagePermissionTypeRadio" value="view"/>
                <label for="restrictViewRadio">Restrict viewing of this page</label>
                <input id="restrictEditRadio" class="radio" type="radio" name="pagePermissionTypeRadio" value="edit"/>
                <label for="restrictEditRadio">Restrict editing of this page</label>
            </div>
        </div>
        <div id="page-permissions-input" class="page-permissions-label-rows">
            <div class="page-permissions-label">To:</div>
            <div id="page-permissions-chooser-box">
                                    <span id="page-permissions-choose-me" class="aui-button normal">
                        <a href="#">
                            <img src="/images/icons/profilepics/default.png" alt="Me"/>
                            Me
                        </a>
                        <span class="remote-user-name hidden">guyh</span>
                    </span>
                                <span id="page-permissions-choose-user" class="aui-button">











<a id='userpicker-popup-link'  href='#' onClick="var picker = window.open('/spaces/openuserpicker.action?key=SPD&amp;startIndex=0&amp;onPopupSubmit=AJS.PagePermissions.addUserPermissions', 'EntitiesPicker', 'status=yes,resizable=yes,top=100,left=200,width=700,height=680,scrollbars=yes'); picker.focus(); return false;">
    				    <img src="/s/zh_CN-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/_/images/icons/user_16.png" height=16 width=16 border=0 align="absmiddle"  title="Choose users" />
						    Person...
	        </a>


                </span>
                <span id="page-permissions-choose-group" class="aui-button">











<a id='grouppicker-popup-link'  href='#' onClick="var picker = window.open('/spaces/opengrouppicker.action?key=SPD&amp;startIndex=0&amp;actionName=dosearchgroups.action&amp;onPopupSubmit=AJS.PagePermissions.addGroupPermissions', 'EntitiesPicker', 'status=yes,resizable=yes,top=100,left=200,width=580,height=550,scrollbars=yes'); picker.focus(); return false;">
    				    <img src="/s/zh_CN-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/_/images/icons/group_16.png" height=16 width=16 border=0 align="absmiddle"  title="Choose groups" />
						    Group...
	        </a>


                </span>
            </div>
            <div id="page-permissions-input-box">
                <input id="page-permissions-names-input" class="autocomplete-user-or-group text" type="text" name="permissionNames"
                    placeholder="Enter user or group name:"
                    data-max="10" data-none-message="No matches"
                    data-target="#page-permissions-names-hidden"
                    data-dropdown-target="#page-perms-name-dropdown-wrapper" data-resize-to-input="true"
                    size="30"/>
                <input
    type="hidden"
                            id="page-permissions-names-hidden"           />                <button class="aui-button" id="add-typed-names">Restrict</button>
                <div id="page-perms-name-dropdown-wrapper" class="aui-dd-parent autocomplete autocomplete-user-or-group-target"></div>
            </div>
        </div>
    </div>
    <div id="page-permissions-tables">
        <div id="page-permissions-table-div">
                        <table id="page-permissions-table" class="page-permissions-table">
                <tr id="page-permissions-no-views" class="marker-row">
                    <td colspan="3" class="page-permissions-marker-cell">
                            <span class="aui-icon aui-icon-small aui-iconfont-view"></span>
                        <span>No view restrictions are defined for this page</span>
                    </td>
                </tr>
                <tr id="page-permissions-no-edits" class="marker-row">
                    <td colspan="3" class="page-permissions-marker-cell">
                            <span class="aui-icon aui-icon-small edit-icon"></span>
                        <span>No edit restrictions are defined for this page</span>
                    </td>
                </tr>
            </table>
        </div>
        <div id="page-inherited-permissions-table-div" class="hidden">
            <span id="page-inherited-permissions-table-desc">
                <a class="icon twisty-closed">Show/Hide</a>
                <a id="toggle-inherited-permissions" title="Click to see inherited restrictions">This page has restricted parent pages. It can only be seen by users who can see those parent pages.</a>
            </span>
            <div id="page-inherited-permissions-tables" class="hidden page-inheritance-togglable"></div>
        </div>
    </div>
</div>
</script>

<!-- End restrictions section -->


<div id="page-metadata-start" class="assistive"></div>
        <div class="wiki-content">
                           <h3 id="diy_1线程与10线程-测试环境：">测试环境：</h3><p><span>1、物理机 8C32G；</span></p><p><span>&nbsp;</span><span>2、 索引量：25606；&nbsp;</span></p><p><span>&nbsp;</span><span>3、JVM参数配置：&nbsp;-Xms2G -Xmx2G -Xmn600M -Xss512k -XX:PermSize=128m -XX:CMSInitiatingOccupancyFraction=70 -XX:SurvivorRatio=1 -XX:MaxTenuringThreshold=11；</span></p><p><span>&nbsp;</span><span>4、半小时性能测试</span></p><p><span>&nbsp;</span><span>5、测试版本：diy_engine_v2.1.4_t2014_12_08_18_42_20</span></p><p><span><br></span></p><h3 id="diy_1线程与10线程-测试结果："><span>测试结果：</span></h3><div class="table-wrap">
                           <table class="confluenceTable tablesorter"><thead><tr class="sortableHeader"><th class="confluenceTh sortableHeader" data-column="0"><div class="tablesorter-header-inner">线程数</div></th><th class="confluenceTh sortableHeader" data-column="1"><div class="tablesorter-header-inner">CPU利用率</div></th><th class="confluenceTh sortableHeader" data-column="2"><div class="tablesorter-header-inner">每秒处理http请求的个数</div></th><th class="confluenceTh sortableHeader" data-column="3"><div class="tablesorter-header-inner">90%的request响应时间</div></th><th class="confluenceTh sortableHeader" data-column="4"><div class="tablesorter-header-inner">最大响应时间</div></th></tr></thead><tbody><tr><td class="confluenceTd">1</td><td class="confluenceTd">12.78%</td><td class="confluenceTd">140.2</td><td class="confluenceTd">13<span>ms</span></td><td class="confluenceTd">201ms</td></tr><tr><td class="confluenceTd">10</td><td class="confluenceTd">76.06%</td><td class="confluenceTd">1171.9</td><td class="confluenceTd">18<span>ms</span></td><td class="confluenceTd">1012<span>ms</span></td></tr></tbody></table>
                           </div>
                           <p>&nbsp;</p><h3 id="diy_1线程与10线程-1个线程"><span>1个线程</span></h3><p><span>&nbsp;</span>CPU利用率曲线：</p><p><img class="confluence-embedded-image" src="D:\testresult\diy\LPresult_figure\LPresult_figure_20150616164400\[1]averageCPU_cpu_1_150615191427_log.png?version=1&amp;modificationDate=1418290879000&amp;api=v2" data-image-src="D:\testresult\diy\LPresult_figure\LPresult_figure_20150616164400\[1]averageCPU_cpu_1_150615191427_log.png?version=1&amp;modificationDate=1418290879000&amp;api=v2"></p><p>平均CPU利用率：12.78%</p><p>内存使用情况：</p><p><img class="confluence-embedded-image" src="/download/attachments/58582949/image2014-12-11%2017%3A35%3A8.png?version=1&amp;modificationDate=1418290879000&amp;api=v2" data-image-src="/download/attachments/58582949/image2014-12-11%2017%3A35%3A8.png?version=1&amp;modificationDate=1418290879000&amp;api=v2"></p><p><img class="confluence-embedded-image" src="/download/attachments/58582949/image2014-12-11%2017%3A35%3A41.png?version=1&amp;modificationDate=1418290879000&amp;api=v2" data-image-src="/download/attachments/58582949/image2014-12-11%2017%3A35%3A41.png?version=1&amp;modificationDate=1418290879000&amp;api=v2"></p><p>吞吐量：</p><p><img class="confluence-embedded-image" src="/download/attachments/58582949/image2014-12-11%2017%3A32%3A50.png?version=1&amp;modificationDate=1418290879000&amp;api=v2" data-image-src="/download/attachments/58582949/image2014-12-11%2017%3A32%3A50.png?version=1&amp;modificationDate=1418290879000&amp;api=v2"></p><h3 id="diy_1线程与10线程-10个线程">10个线程</h3><p>&nbsp;CPU利用率曲线：</p><p><img class="confluence-embedded-image" src="/download/attachments/58582949/image2014-12-11%2017%3A36%3A47.png?version=1&amp;modificationDate=1418290879000&amp;api=v2" data-image-src="/download/attachments/58582949/image2014-12-11%2017%3A36%3A47.png?version=1&amp;modificationDate=1418290879000&amp;api=v2"></p><p>平均CPU利用率：76.06%</p><p>内存使用情况：</p><p><img class="confluence-embedded-image" src="/download/attachments/58582949/image2014-12-11%2017%3A39%3A22.png?version=1&amp;modificationDate=1418290879000&amp;api=v2" data-image-src="/download/attachments/58582949/image2014-12-11%2017%3A39%3A22.png?version=1&amp;modificationDate=1418290879000&amp;api=v2"></p><p><img class="confluence-embedded-image" src="/download/attachments/58582949/image2014-12-11%2017%3A39%3A40.png?version=1&amp;modificationDate=1418290879000&amp;api=v2" data-image-src="/download/attachments/58582949/image2014-12-11%2017%3A39%3A40.png?version=1&amp;modificationDate=1418290879000&amp;api=v2"></p><p>吞吐量：</p><p><img class="confluence-embedded-image" src="/download/attachments/58582949/image2014-12-11%2017%3A39%3A51.png?version=1&amp;modificationDate=1418290879000&amp;api=v2" data-image-src="/download/attachments/58582949/image2014-12-11%2017%3A39%3A51.png?version=1&amp;modificationDate=1418290879000&amp;api=v2"></p><p><span><br></span></p>

        </div>

        <!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:dc="http://purl.org/dc/elements/1.1/"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/">
         <rdf:Description
    rdf:about="http://conf.ctripcorp.com/pages/viewpage.action?pageId=58582949"
    dc:identifier="http://conf.ctripcorp.com/pages/viewpage.action?pageId=58582949"
    dc:title="diy_1线程与10线程"
    trackback:ping="http://conf.ctripcorp.com/rpc/trackback/58582949"/>
</rdf:RDF>
-->


























<div id="comments-section" class="pageSection group">




            <div class="bottom-comment-panels comment-panels">












            </div>

                        <div id="comments-actions" class="aui-toolbar noprint" style="display: none;">
                <p class="toolbar-group">
                    <span class="toolbar-item"><a href="/pages/viewpage.action?pageId=58582949&amp;showComments=true&amp;showCommentArea=true#addcomment" id="add-comment-rte" accesskey="m" class="toolbar-trigger">Add Comment</a></span>
                </p>
            </div>
            </div>



</div>




















    <br class="clear">
</div>

    </div>
</div>





    </div>


<div id="content-hover-0" class="ajs-content-hover" style="display: none;"><div class="contents" style="width: 300px;"></div></div><div id="content-hover-1" class="ajs-content-hover" style="display: none;"><div class="contents" style="width: 300px;"></div></div><div id="fancybox-tmp" style="padding: 40px;"></div><div id="fancybox-loading" style="display: none;"><div></div></div><div id="fancybox-overlay" style="opacity: 0.5; cursor: pointer; height: 655px; display: none; background-color: rgb(119, 119, 119);"></div><div id="fancybox-wrap" style="width: 481px; height: auto; top: 163px; left: 379px; display: none; opacity: 1;"><div id="fancybox-outer"><div class="fancybox-bg" id="fancybox-bg-n"></div><div class="fancybox-bg" id="fancybox-bg-ne"></div><div class="fancybox-bg" id="fancybox-bg-e"></div><div class="fancybox-bg" id="fancybox-bg-se"></div><div class="fancybox-bg" id="fancybox-bg-s"></div><div class="fancybox-bg" id="fancybox-bg-sw"></div><div class="fancybox-bg" id="fancybox-bg-w"></div><div class="fancybox-bg" id="fancybox-bg-nw"></div><div id="fancybox-content" style="border-width: 0px; width: 481px; height: 289px;"></div><a id="fancybox-close" style="display: none;"></a><div id="fancybox-title" style="display: none;"></div><a href="javascript:;" id="fancybox-left" style="display: none;"><span class="fancy-ico" id="fancybox-left-ico"></span></a><a href="javascript:;" id="fancybox-right" style="display: none;"><span class="fancy-ico" id="fancybox-right-ico"></span></a></div></div><div id="content-hover-shadow" style="display: none;"><div class="tl"></div><div class="tr"></div><div class="l"></div><div class="r"></div><div class="bl"></div><div class="br"></div><div class="b"></div></div><div class="qr-notice aui-message warning"></div><div id="fileuploadShim" style="position: relative; z-index: 0;"></div><div id="p19o2s0om5qg019vaftl2vo1gn0_html5_container" class="plupload html5" style="position: absolute; width: 1263px; height: 0px; overflow: hidden; z-index: -1; opacity: 0; top: 341px; left: 0px; background: transparent;"><input id="p19o2s0om5qg019vaftl2vo1gn0_html5" style="font-size: 999px; position: absolute; width: 100%; height: 100%;" type="file" accept="" multiple="multiple"></div><div id="editor-preload-container" style="display: none;">
<div class="hidden">



<content tag="breadcrumbs">


    <ol id="quickedit-breadcrumbs">


        <li class="first">


                    <span class=""><a href="/display/SPD">搜索产品研发部</a></span>
                                                </li><li id="ellipsis" title="Show all breadcrumbs"><span><strong>…</strong></span></li>


        <li class="hidden-crumb">


                    <span class=""><a href="/pages/viewpage.action?pageId=35489476">搜索产品研发部 首页</a></span>


        </li><li class="hidden-crumb">


                    <span class=""><a href="/pages/viewpage.action?pageId=45517677">【搜索】测试—性能/压力</a></span>


        </li><li>


                    <span class=""><a href="/pages/viewpage.action?pageId=58582307">【Diy】</a></span>


        </li><li>


                    <span class="edited-page-title"><a href="/pages/viewpage.action?pageId=58582949">diy_1线程与10线程</a></span>
                </li></ol>

</content>
</div>


<div id="editor-precursor">
    <div class="cell">

        <div id="content-title-div">


<div class="field-group
    ">
    <label id="content-title-label" for="content-title">

        </label>

                <input type="text" name="title" id="content-title" value="diy_1线程与10线程" tabindex="1" class="text   pagetitle" autocomplete="off" placeholder="">
                      </div>        </div>

        <div id="editor-messages">


<div id="heartbeat-div" class="hidden">
    <div class="aui-message warning closeable">
            <span class="aui-icon icon-warning"></span>
        This page is being edited by <span id="other-users-span"></span>.
    </div>
</div>


        </div>
        <div id="all-messages">

<div id="action-messages">
                        </div>
        </div>
    </div>
</div>

<script type="text/x-template" title="editor-css">
    <link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/1.0/_/download/batch/confluence.web.resources:panel-styles/confluence.web.resources:panel-styles.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/1.0/_/download/batch/confluence.web.resources:content-styles/confluence.web.resources:content-styles.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/1.0/_/download/batch/confluence.web.resources:panel-styles/confluence.web.resources:panel-styles.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.0/_/download/batch/com.atlassian.auiplugin:aui-experimental-page-layout-typography/com.atlassian.auiplugin:aui-experimental-page-layout-typography.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.0/_/download/batch/com.atlassian.auiplugin:aui-experimental-avatars/com.atlassian.auiplugin:aui-experimental-avatars.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.0/_/download/batch/com.atlassian.auiplugin:aui-experimental-page-layout/com.atlassian.auiplugin:aui-experimental-page-layout.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_/download/batch/com.atlassian.confluence.editor:editor-content-styles/com.atlassian.confluence.editor:editor-content-styles.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.0/_/download/batch/com.atlassian.auiplugin:aui-experimental-lozenge/com.atlassian.auiplugin:aui-experimental-lozenge.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2.10/_/download/batch/com.atlassian.confluence.plugins.status-macro:view_content_status/com.atlassian.confluence.plugins.status-macro:view_content_status.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/2.10/_/download/batch/com.atlassian.confluence.plugins.status-macro:editor_content_status/com.atlassian.confluence.plugins.status-macro:editor_content_status.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_/download/batch/com.atlassian.confluence.plugins.confluence-templates:variable-editor-content-styles/com.atlassian.confluence.plugins.confluence-templates:variable-editor-content-styles.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/3.6.2/_/download/batch/confluence.extra.attachments:attachments-css/confluence.extra.attachments:attachments-css.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_/download/batch/com.atlassian.confluence.plugins.confluence-inline-tasks:inline-tasks-styles/com.atlassian.confluence.plugins.confluence-inline-tasks:inline-tasks-styles.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/1/_/styles/colors.css?spaceKey=SPD" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_/download/resources/com.atlassian.confluence.plugins.doctheme:documentation/default-theme.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_/download/resources/com.atlassian.confluence.plugins.doctheme:documentation/doc-theme.css" media="all">
<link type="text/css" rel="stylesheet" href="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_/download/resources/com.atlassian.confluence.plugins.doctheme:documentation/splitter.css" media="all">

</script>













<div class="editor-container">


            <div id="image-properties-tab-items" class="hidden">
                <div title="Effects" data-weight="10">image-effects</div>
            <div title="Title" data-weight="20">image-attributes</div>
    </div>


<div id="link-browser-tab-items" class="hidden">
                <div title="Search" data-weight="10">search</div>
            <div title="Recently Viewed" data-weight="20">recentlyviewed</div>
            <div title="Attachments" data-weight="30">attachments</div>
            <div title="Web Link" data-weight="40">weblink</div>
            <div title="Advanced" data-weight="50">advanced</div>
    </div>












        <div id="toolbar">
        <div id="rte-toolbar" class="aui-toolbar aui-toolbar2">

            <div class="aui-toolbar2-primary">
                <ul class="aui-buttons">
                                        <li id="format-dropdown" class="toolbar-item toolbar-dropdown">
                        <div class="aui-dd-parent">
                            <a id="format-dropdown-display" href="#" class="toolbar-trigger aui-dd-trigger aui-button" data-control-id="formatselect">
                                <span class="dropdown-text">Paragraph</span>
                                    <span class="icon icon-dropdown "></span>
                            </a>
                            <ul id="format-dropdown-display-menu" class="aui-dropdown hidden">
                                    <li class="dropdown-item format-p" data-format="p" data-tooltip="Paragraph (Ctrl+0)">
        <a class="item-link" href="#">Paragraph</a>
    </li>
                                    <li class="dropdown-item format-h1" data-format="h1" data-tooltip="Heading 1 (Ctrl+1)">
        <a class="item-link" href="#">Heading 1</a>
    </li>
                                    <li class="dropdown-item format-h2" data-format="h2" data-tooltip="Heading 2 (Ctrl+2)">
        <a class="item-link" href="#">Heading 2</a>
    </li>
                                    <li class="dropdown-item format-h3" data-format="h3" data-tooltip="Heading 3 (Ctrl+3)">
        <a class="item-link" href="#">Heading 3</a>
    </li>
                                    <li class="dropdown-item format-h4" data-format="h4" data-tooltip="Heading 4 (Ctrl+4)">
        <a class="item-link" href="#">Heading 4</a>
    </li>
                                    <li class="dropdown-item format-h5" data-format="h5" data-tooltip="Heading 5 (Ctrl+5)">
        <a class="item-link" href="#">Heading 5</a>
    </li>
                                    <li class="dropdown-item format-h6" data-format="h6" data-tooltip="Heading 6 (Ctrl+6)">
        <a class="item-link" href="#">Heading 6</a>
    </li>
                                    <li class="dropdown-item format-pre" data-format="pre" data-tooltip="Preformatted (Ctrl+7)">
        <a class="item-link" href="#">Preformatted</a>
    </li>
                                    <li class="dropdown-item format-blockquote" data-format="blockquote" data-tooltip="Quote (Ctrl+8)">
        <a class="item-link" href="#">Quote</a>
    </li>
                            </ul>
                        </div>
                    </li>
                </ul>

                <ul class="aui-buttons">

                <li class="toolbar-item aui-button" id="rte-button-bold" data-tooltip="Bold (Ctrl+B)">
        <a class="toolbar-trigger" href="#" data-control-id="bold">
                <span class="icon icon-bold ">Bold</span>
        </a>
    </li>

                <li class="toolbar-item aui-button" id="rte-button-italic" data-tooltip="Italic (Ctrl+I)">
        <a class="toolbar-trigger" href="#" data-control-id="italic">
                <span class="icon icon-italic ">Italic</span>
        </a>
    </li>

                <li class="toolbar-item aui-button" id="rte-button-underline" data-tooltip="Underline (Ctrl+U)">
        <a class="toolbar-trigger" href="#" data-control-id="underline">
                <span class="icon icon-underline ">Underline</span>
        </a>
    </li>
                                        <li id="color-picker-control" class="toolbar-item toolbar-splitbutton">
                        <a class="toolbar-trigger aui-button" href="#" id="rte-button-color" data-color="003366" data-tooltip="Colour">
                                <span class="icon icon-textcolor ">Colour picker</span>
                            <span class="selected-color"></span>
                        </a>
                        <div class="aui-dd-parent">
                            <a class="toolbar-trigger aui-dd-trigger aui-button" href="#" id="rte-button-color-selector" data-control-id="colorSelector" data-tooltip="More colours">
                                    <span class="icon icon-dropdown ">More colours</span>
                            </a>
                            <div class="color-picker-container">
                                <div class="color-picker aui-dropdown hidden">
                                    <ul>
            <li><a href="#" style="background-color: #000000" data-color="000000">&nbsp;</a></li>
            <li><a href="#" style="background-color: #993300" data-color="993300">&nbsp;</a></li>
            <li><a href="#" style="background-color: #333300" data-color="333300">&nbsp;</a></li>
            <li><a href="#" style="background-color: #003300" data-color="003300">&nbsp;</a></li>
            <li><a href="#" style="background-color: #003366" data-color="003366">&nbsp;</a></li>
            <li><a href="#" style="background-color: #000080" data-color="000080">&nbsp;</a></li>
            <li><a href="#" style="background-color: #333399" data-color="333399">&nbsp;</a></li>
            <li><a href="#" style="background-color: #333333" data-color="333333">&nbsp;</a></li>
            <li><a href="#" style="background-color: #800000" data-color="800000">&nbsp;</a></li>
            <li><a href="#" style="background-color: #FF6600" data-color="FF6600">&nbsp;</a></li>
            <li><a href="#" style="background-color: #808000" data-color="808000">&nbsp;</a></li>
            <li><a href="#" style="background-color: #008000" data-color="008000">&nbsp;</a></li>
            <li><a href="#" style="background-color: #008080" data-color="008080">&nbsp;</a></li>
            <li><a href="#" style="background-color: #0000FF" data-color="0000FF">&nbsp;</a></li>
            <li><a href="#" style="background-color: #666699" data-color="666699">&nbsp;</a></li>
            <li><a href="#" style="background-color: #808080" data-color="808080">&nbsp;</a></li>
            <li><a href="#" style="background-color: #FF0000" data-color="FF0000">&nbsp;</a></li>
            <li><a href="#" style="background-color: #FF9900" data-color="FF9900">&nbsp;</a></li>
            <li><a href="#" style="background-color: #99CC00" data-color="99CC00">&nbsp;</a></li>
            <li><a href="#" style="background-color: #339966" data-color="339966">&nbsp;</a></li>
            <li><a href="#" style="background-color: #33CCCC" data-color="33CCCC">&nbsp;</a></li>
            <li><a href="#" style="background-color: #3366FF" data-color="3366FF">&nbsp;</a></li>
            <li><a href="#" style="background-color: #800080" data-color="800080">&nbsp;</a></li>
            <li><a href="#" style="background-color: #999999" data-color="999999">&nbsp;</a></li>
            <li><a href="#" style="background-color: #FF00FF" data-color="FF00FF">&nbsp;</a></li>
            <li><a href="#" style="background-color: #FFCC00" data-color="FFCC00">&nbsp;</a></li>
            <li><a href="#" style="background-color: #FFFF00" data-color="FFFF00">&nbsp;</a></li>
            <li><a href="#" style="background-color: #00FF00" data-color="00FF00">&nbsp;</a></li>
            <li><a href="#" style="background-color: #00FFFF" data-color="00FFFF">&nbsp;</a></li>
            <li><a href="#" style="background-color: #00CCFF" data-color="00CCFF">&nbsp;</a></li>
            <li><a href="#" style="background-color: #993366" data-color="993366">&nbsp;</a></li>
            <li><a href="#" style="background-color: #C0C0C0" data-color="C0C0C0">&nbsp;</a></li>
            <li><a href="#" style="background-color: #FF99CC" data-color="FF99CC">&nbsp;</a></li>
            <li><a href="#" style="background-color: #FFCC99" data-color="FFCC99">&nbsp;</a></li>
            <li><a href="#" style="background-color: #FFFF99" data-color="FFFF99">&nbsp;</a></li>
            <li><a href="#" style="background-color: #CCFFCC" data-color="CCFFCC">&nbsp;</a></li>
            <li><a href="#" style="background-color: #CCFFFF" data-color="CCFFFF">&nbsp;</a></li>
            <li><a href="#" style="background-color: #99CCFF" data-color="99CCFF">&nbsp;</a></li>
            <li><a href="#" style="background-color: #CC99FF" data-color="CC99FF">&nbsp;</a></li>
            <li><a href="#" style="background-color: #FFFFFF" data-color="FFFFFF">&nbsp;</a></li>
    </ul>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li id="more-menu" class="toolbar-item toolbar-dropdown">
                        <div class="aui-dd-parent">
                            <a id="rte-button-more" href="#" class="toolbar-trigger aui-dd-trigger aui-button" data-tooltip="More">
                                    <span class="icon icon-more ">Formatting</span>
                                    <span class="icon icon-dropdown "></span>
                            </a>
                            <div id="rte-button-more-menu" class="aui-dropdown grouped hidden">
                                <div class="grouped-dropdown-item">
                                    <ul>
                                                                <li class="dropdown-item more-menu-trigger" data-control-id="strikethrough" data-tooltip="Strikethrough (Ctrl+Shift+S)">
        <a id="rte-strikethrough" class="item-link" href="#">
                <span class="icon icon-check hidden"></span>
Strikethrough
        </a>
    </li>
                                                                 <li class="dropdown-item more-menu-trigger" data-control-id="sub" data-tooltip="">
        <a id="rte-sub" class="item-link" href="#">
                <span class="icon icon-check hidden"></span>
Subscript
        </a>
    </li>
                                                                 <li class="dropdown-item more-menu-trigger" data-control-id="sup" data-tooltip="">
        <a id="rte-sup" class="item-link" href="#">
                <span class="icon icon-check hidden"></span>
Superscript
        </a>
    </li>
                                                        <li class="dropdown-item more-menu-trigger" data-control-id="monospace" data-tooltip="Format text with monospaced font">
        <a id="rte-monospace" class="item-link" href="#">
                <span class="icon icon-check hidden"></span>
Monospace
        </a>
    </li>

                                                                                                                    </ul>
                                </div>
                                <div class="grouped-dropdown-item">
                                    <ul>
                                            <li class="dropdown-item more-menu-trigger no-icon" data-format="removeformat" data-tooltip="Clears formatting on currently selected text">
        <a id="rte-removeformat" class="item-link" href="#">
            Clear Formatting
        </a>
    </li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                    </li>
                </ul>

                <ul class="aui-buttons">

                <li class="toolbar-item aui-button" id="rte-button-bullist" data-tooltip="Bullet list (Ctrl+Shift+B)">
        <a class="toolbar-trigger" href="#" data-control-id="bullist">
                <span class="icon icon-bullist ">Bullet list</span>
        </a>
    </li>

                <li class="toolbar-item aui-button" id="rte-button-numlist" data-tooltip="Numbered list (Ctrl+Shift+N)">
        <a class="toolbar-trigger" href="#" data-control-id="numlist">
                <span class="icon icon-numlist ">Numbered list</span>
        </a>
    </li>

                <li class="toolbar-item aui-button" id="rte-button-tasklist" data-tooltip="Task list ([ then ])">
        <a class="toolbar-trigger" href="#" data-control-id="tasklist">
                <span class="icon icon-tasklist ">Task list</span>
        </a>
    </li>
                                    </ul>

                <ul class="aui-buttons">

                <li class="toolbar-item aui-button" id="rte-button-outdent" data-tooltip="Outdent">
        <a class="toolbar-trigger" href="#" data-control-id="outdent">
                <span class="icon icon-outdent ">Outdent</span>
        </a>
    </li>

                <li class="toolbar-item aui-button" id="rte-button-indent" data-tooltip="Indent">
        <a class="toolbar-trigger" href="#" data-control-id="indent">
                <span class="icon icon-indent ">Indent</span>
        </a>
    </li>
                </ul>

                <ul class="aui-buttons">

                <li class="toolbar-item aui-button" id="rte-button-justifyleft" data-tooltip="Align left">
        <a class="toolbar-trigger" href="#" data-control-id="justifyleft">
                <span class="icon icon-justifyleft ">Align left</span>
        </a>
    </li>

                <li class="toolbar-item aui-button" id="rte-button-justifycenter" data-tooltip="Align center">
        <a class="toolbar-trigger" href="#" data-control-id="justifycenter">
                <span class="icon icon-justifycenter ">Align center</span>
        </a>
    </li>

                <li class="toolbar-item aui-button" id="rte-button-justifyright" data-tooltip="Align right">
        <a class="toolbar-trigger" href="#" data-control-id="justifyright">
                <span class="icon icon-justifyright ">Align right</span>
        </a>
    </li>
                </ul>

                <ul class="aui-buttons">
                    <li class="toolbar-item" data-tooltip="Insert Link (Ctrl+K)">
                        <a id="rte-button-link" class="toolbar-trigger aui-button" href="#" data-control-id="linkbrowserButton">
                                <span class="icon icon-link "></span>
                            <span class="trigger-text">Link</span>
                        </a>
                    </li>
                </ul>

                <ul class="aui-buttons">
                    <li class="toolbar-item toolbar-dropdown" id="insert-table-dropdown">
                        <div class="aui-dd-parent">
                            <a href="#" class="toolbar-trigger aui-dd-trigger aui-button" id="rte-button-insert-table" data-tooltip="Insert Table">
                                    <span class="icon icon-table "></span>
                                <span class="dropdown-text">Table</span>
                                    <span class="icon icon-dropdown "></span>
                            </a>

                            <div id="table-picker-container" class="hidden">
                                <div class="table-picker-box" data-tooltip="Hold SHIFT for a table without a heading.">
                                    <div class="table-picker-background">
                                        <div class="picker picker-cell"></div>
                                        <div class="picker picker-heading heading"></div>
                                        <div class="picker picker-selected-cell"></div>
                                        <div class="picker picker-selected-heading heading"></div>
                                    </div>
                                    <p class="desc"></p>
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>


                <ul class="aui-buttons">
                    <li class="toolbar-item toolbar-dropdown" id="insert-menu">
                        <div class="aui-dd-parent">
                            <a href="#" class="toolbar-trigger aui-dd-trigger aui-button" id="rte-button-insert" data-tooltip="Insert More Content">
                                    <span class="icon icon-insert "></span>
                                <span class="dropdown-text">Insert</span>
                                    <span class="icon icon-dropdown "></span>
                            </a>

                            <div id="insert-menu-options" class="aui-dropdown grouped hidden">
                                <div class="grouped-dropdown-item">
                                    <span class="assistive">Insert Content</span>
                                    <ul id="content-insert-list">


        <li class="dropdown-item content-image" data-command="mceConfimage" data-tooltip="Insert Image (Ctrl+M)">
        <a id="rte-insert-image" class="item-link" href="#">
                <span class="icon "></span>
 Image
        </a>
    </li>


        <li class="dropdown-item content-link" data-control-id="linkbrowserButton" data-tooltip="Insert Link (Ctrl+K)">
        <a id="rte-insert-link" class="item-link" href="#">
                <span class="icon "></span>
 Link
        </a>
    </li>


        <li class="dropdown-item content-attachment" data-command="mceConfAttachments" data-tooltip="Insert Attachment">
        <a id="rte-insert-attachment" class="item-link" href="#">
                <span class="icon "></span>
 Attachment
        </a>
    </li>


        <li class="dropdown-item content-symbol" data-command="confCharmap" data-tooltip="Insert Symbol">
        <a id="rte-insert-symbol" class="item-link" href="#">
                <span class="icon "></span>
 Symbol
        </a>
    </li>


        <li class="dropdown-item content-emoticon" data-command="mceEmotion" data-tooltip="Insert Emoticon">
        <a id="rte-insert-emoticon" class="item-link" href="#">
                <span class="icon "></span>
 Emoticon
        </a>
    </li>


        <li class="dropdown-item content-wikimarkup" data-command="InsertWikiMarkup" data-tooltip="Insert Wiki Markup (Ctrl+Shift+D)">
        <a id="rte-insert-wikimarkup" class="item-link" href="#">
                <span class="icon "></span>
 Wiki Markup
        </a>
    </li>


        <li class="dropdown-item content-hr" data-command="InsertHorizontalRule" data-tooltip="Insert horizontal rule (----)">
        <a id="rte-insert-hr" class="item-link" href="#">
                <span class="icon "></span>
 Horizontal rule
        </a>
    </li>


        <li class="dropdown-item content-tasklist" data-command="InsertInlineTaskListNoToggle" data-tooltip="Insert Task List ([ then ])">
        <a id="rte-insert-tasklist" class="item-link" href="#">
                <span class="icon "></span>
 Task List
        </a>
    </li>
                                                                            </ul>
                                </div>
                                <div class="grouped-dropdown-item">
                                    <span class="assistive">Insert Macro</span>
                                    <ul id="macro-insert-list">
                                                                                                                                                                                <li class="dropdown-item macro-insertmention-button" data-macro-name="insertmention-button" data-tooltip="Insert 'User Mention' macro">
        <a id="insertmention-button" class="item-link" href="#">
                <span class="icon "></span>
 User Mention
        </a>
    </li>
                                                                                                <li class="dropdown-item macro-info" data-macro-name="info" data-tooltip="Insert 'Info' macro">
        <a id="info" class="item-link" href="#">
                <span class="icon "></span>
 Info
        </a>
    </li>
                                                                                                <li class="dropdown-item macro-jiralink" data-macro-name="jiralink" data-tooltip="Insert 'JIRA Issue' macro">
        <a id="jiralink" class="item-link" href="#">
                <span class="icon "></span>
 JIRA Issue
        </a>
    </li>
                                                                                                <li class="dropdown-item macro-status" data-macro-name="status" data-tooltip="Insert 'Status' macro">
        <a id="status" class="item-link" href="#">
                <span class="icon "></span>
 Status
        </a>
    </li>
                                                                                                <li class="dropdown-item macro-gallery" data-macro-name="gallery" data-tooltip="Insert 'Gallery' macro">
        <a id="gallery" class="item-link" href="#">
                <span class="icon "></span>
 Gallery
        </a>
    </li>
                                                                                                <li class="dropdown-item macro-toc" data-macro-name="toc" data-tooltip="Insert 'Table of Contents' macro">
        <a id="toc" class="item-link" href="#">
                <span class="icon "></span>
 Table of Contents
        </a>
    </li>


        <li class="dropdown-item content-macro" data-command="mceConfMacroBrowser" data-tooltip="Open the macro browser (Ctrl+Shift+A)">
        <a id="rte-insert-macro" class="item-link" href="#">
                <span class="icon "></span>
 Other Macros
        </a>
    </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>
                                <ul class="aui-buttons">
                    <li id="pagelayout-menu" class="toolbar-item toolbar-dropdown">
                        <div class="aui-dd-parent">
                            <a href="#" class="toolbar-trigger aui-dd-trigger aui-button" id="rte-button-pagelayout" data-tooltip="Page Layout">
                                    <span class="icon icon-layout pagelayout-default">Page Layout</span>
                                    <span class="icon icon-dropdown "></span>
                            </a>

                            <ul id="pagelayout-menu-options" class="aui-dropdown hidden">
                                <li class="dropdown-item" data-tooltip="No Layout">
    <a href="#" class="item-link" data-atlassian-layout="{&quot;name&quot;: &quot;pagelayout-none&quot;, &quot;columns&quot;: 0   }">
            <span class="icon icon-check hidden"></span>
            <span class="icon icon-layout pagelayout-none">No Layout</span>
    </a>
</li>
                                <li class="dropdown-item" data-tooltip="Two column (simple)">
    <a href="#" class="item-link" data-atlassian-layout="{&quot;name&quot;: &quot;pagelayout-two-simple&quot;, &quot;columns&quot;: [&quot;&quot;, &quot;&quot;]   }">
            <span class="icon icon-check hidden"></span>
            <span class="icon icon-layout pagelayout-two-simple">Two column (simple)</span>
    </a>
</li>
                                <li class="dropdown-item" data-tooltip="Two column (simple, left sidebar)">
    <a href="#" class="item-link" data-atlassian-layout="{&quot;name&quot;: &quot;pagelayout-two-simple-left&quot;, &quot;columns&quot;: [&quot;aside&quot;, &quot;large&quot;]   }">
            <span class="icon icon-check hidden"></span>
            <span class="icon icon-layout pagelayout-two-simple-left">Two column (simple, left sidebar)</span>
    </a>
</li>
                                <li class="dropdown-item" data-tooltip="Two column (simple, right sidebar)">
    <a href="#" class="item-link" data-atlassian-layout="{&quot;name&quot;: &quot;pagelayout-two-simple-right&quot;, &quot;columns&quot;: [&quot;large&quot;, &quot;aside&quot;]   }">
            <span class="icon icon-check hidden"></span>
            <span class="icon icon-layout pagelayout-two-simple-right">Two column (simple, right sidebar)</span>
    </a>
</li>
                                <li class="dropdown-item" data-tooltip="Three column (simple)">
    <a href="#" class="item-link" data-atlassian-layout="{&quot;name&quot;: &quot;pagelayout-three-simple&quot;, &quot;columns&quot;: [&quot;&quot;, &quot;&quot;, &quot;&quot;]   }">
            <span class="icon icon-check hidden"></span>
            <span class="icon icon-layout pagelayout-three-simple">Three column (simple)</span>
    </a>
</li>
                                <li class="dropdown-item" data-tooltip="Two column">
    <a href="#" class="item-link" data-atlassian-layout="{&quot;name&quot;: &quot;pagelayout-two&quot;, &quot;columns&quot;: [&quot;&quot;, &quot;&quot;] , &quot;header&quot;: true  , &quot;footer&quot;:true  }">
            <span class="icon icon-check hidden"></span>
            <span class="icon icon-layout pagelayout-two">Two column</span>
    </a>
</li>
                                <li class="dropdown-item" data-tooltip="Two column (left sidebar)">
    <a href="#" class="item-link" data-atlassian-layout="{&quot;name&quot;: &quot;pagelayout-two-left&quot;, &quot;columns&quot;: [&quot;aside&quot;, &quot;large&quot;] , &quot;header&quot;: true  , &quot;footer&quot;:true  }">
            <span class="icon icon-check hidden"></span>
            <span class="icon icon-layout pagelayout-two-left">Two column (left sidebar)</span>
    </a>
</li>
                                <li class="dropdown-item" data-tooltip="Two column (right sidebar)">
    <a href="#" class="item-link" data-atlassian-layout="{&quot;name&quot;: &quot;pagelayout-two-right&quot;, &quot;columns&quot;: [&quot;large&quot;, &quot;aside&quot;] , &quot;header&quot;: true  , &quot;footer&quot;:true  }">
            <span class="icon icon-check hidden"></span>
            <span class="icon icon-layout pagelayout-two-right">Two column (right sidebar)</span>
    </a>
</li>
                                <li class="dropdown-item" data-tooltip="Three column">
    <a href="#" class="item-link" data-atlassian-layout="{&quot;name&quot;: &quot;pagelayout-three&quot;, &quot;columns&quot;: [&quot;&quot;, &quot;&quot;, &quot;&quot;] , &quot;header&quot;: true  , &quot;footer&quot;:true  }">
            <span class="icon icon-check hidden"></span>
            <span class="icon icon-layout pagelayout-three">Three column</span>
    </a>
</li>
                                <li class="dropdown-item" data-tooltip="Three column (left and right sidebars)">
    <a href="#" class="item-link" data-atlassian-layout="{&quot;name&quot;: &quot;pagelayout-three-sidebars&quot;, &quot;columns&quot;: [&quot;sidebars&quot;, &quot;large&quot;, &quot;sidebars&quot;] , &quot;header&quot;: true  , &quot;footer&quot;:true  }">
            <span class="icon icon-check hidden"></span>
            <span class="icon icon-layout pagelayout-three-sidebars">Three column (left and right sidebars)</span>
    </a>
</li>
                            </ul>
                        </div>
                    </li>
                </ul>

                <ul class="aui-buttons">

                <li class="toolbar-item aui-button" id="rte-button-undo" data-tooltip="Undo (Ctrl+Z)">
        <a class="toolbar-trigger" href="#" data-control-id="undo">
                <span class="icon icon-undo ">Undo</span>
        </a>
    </li>

                <li class="toolbar-item aui-button" id="rte-button-redo" data-tooltip="Redo (Ctrl+Y)">
        <a class="toolbar-trigger" href="#" data-control-id="redo">
                <span class="icon icon-redo ">Redo</span>
        </a>
    </li>
                </ul>


            </div>            <div class="aui-toolbar2-secondary">
                <ul class="aui-buttons">
                        <li class="toolbar-item aui-button" id="rte-button-searchreplace" data-tooltip="Find/Replace">
        <a class="toolbar-trigger" href="#" data-control-id="searchreplace">
                <span class="icon icon-searchreplace ">Find/Replace</span>
        </a>
    </li>
                </ul>
                <ul class="aui-buttons">
                        <li class="toolbar-item aui-button" id="rte-button-help" data-tooltip="Help">
        <a class="toolbar-trigger" href="#" data-control-id="help">
                <span class="icon icon-help ">Keyboard Shortcuts Help</span>
        </a>
    </li>
                </ul>
                <ul class="aui-buttons">
                        <li class="toolbar-item aui-button" id="rte-button-hidetools" data-tooltip="Hide Tools">
        <a class="toolbar-trigger" href="#" data-control-id="hidetools">
                <span class="icon icon-hidetools ">Hide the toolbars</span>
        </a>
    </li>
                        <li class="toolbar-item aui-button" id="rte-button-fullscreen" data-tooltip="Full Screen">
        <a class="toolbar-trigger" href="#" data-control-id="fullscreen">
                <span class="icon icon-fullscreen ">Launch editor full screen</span>
        </a>
    </li>
                </ul>
            </div>        </div>    </div>
    <div id="wysiwyg" class="resize">
        <div id="rte" class="cell editor-default">
            <textarea id="wysiwygTextarea" name="wysiwygContent" class="hidden tinymce-editor"></textarea>
        </div>
    </div>
    <div id="editor-html-source-container" class="hidden">
        <textarea id="editor-html-source" class="monospaceInput"></textarea>
    </div>

    <div id="preview">
                        <div id="previewArea" class="cell">
        </div>
    </div>



<div id="savebar-container">
    <div id="rte-savebar" class="aui-toolbar aui-toolbar2">



        <div class="toolbar-split toolbar-split-row">
            <div class="toolbar-split toolbar-split-left">
            <ul class="aui-buttons">
                                                                                            <li class="toolbar-item aui-button" data-tooltip="Insert Attachment">
                        <a class="toolbar-trigger" href="#" id="rte-button-attachments">
                            <span class="icon icon-attachment"></span>
                            <span class="trigger-text">8 Attachments</span>
                        </a>
                    </li>
                                                                            <li class="toolbar-item aui-button" data-tooltip="Edit Page Labels">
                        <a class="toolbar-trigger" href="#" id="rte-button-labels">
                            <span class="icon icon-labels"></span>
                            <span class="trigger-text">Labels</span>
                        </a>
                    </li>
                            </ul>
                    </div>            <div class="toolbar-split toolbar-split-right">
                            <div class="aui-buttons" id="toolbar-group-minor-edit">
                    <ul class="toolbar-group toolbar-group-watch-page" id="toolbar-group-watch-page-after-comment">
                        <li class="toolbar-item">
                            <label for="watchPage">Watch this page</label>
                            <input id="watchPage" name="watchPageAfterComment" value="true" type="checkbox" checked="checked">
                        </li>
                    </ul>
                                             <span class="rte-toolbar-comment toolbar-item">
                            <input id="versionComment" name="versionComment" placeholder="What did you change?" class="text" type="text" size="35">
                            <label for="versionComment" class="assistive">What did you change?</label>
                        </span>
                                                                 <span class="minor-edit toolbar-item">
                            <input id="notifyWatchers" name="notifyWatchers" value="true" type="checkbox" checked="checked">
                            <label for="notifyWatchers"><span>Notify watchers</span></label>
                        </span>
                                    </div>

                    <div class="aui-buttons">
                <span id="rte-spinner" class="toolbar-item">&nbsp;</span>
            </div>
            <ul class="aui-buttons toolbar-group-edit assistive">
                <li class="toolbar-item">
                    <a id="rte-button-edit" class="toolbar-trigger aui-button" title="Return To Edit Mode" href="#"><span class="trigger-text">Edit</span></a>
                </li>
            </ul>
            <ul class="aui-buttons toolbar-group-preview">
                <li class="toolbar-item">
                    <a id="rte-button-preview" title="Preview" class="toolbar-trigger aui-button" href="#"><span class="trigger-text"><span>Preview</span></span></a>
                </li>
            </ul>


            <ul class="save-button-container">
                                                                                                                                                            <li class="toolbar-item">
                            <button class="toolbar-trigger aui-button aui-button-primary" type="submit" href="#" id="rte-button-publish" name="confirm" value="Save" tabindex="101" title="Save your page">
                                <span class="trigger-text"><span>Save</span></span>
                            </button>
                        </li>
                                                </ul>
                                            <ul class="aui-buttons">
                <li class="toolbar-item toolbar-item-link">
                    <button class="toolbar-trigger aui-button aui-button-link" type="submit" id="rte-button-cancel" value="discard" name="cancel"><span class="trigger-text">Cancel</span></button>
                </li>
            </ul>

        </div>         </div>
                    <div class="toolbar-split toolbar-split-row" id="toolbar-hints-draft-status">
                <div class="toolbar-split toolbar-split-left">
                    <div class="hints hints-open">
                        <span class="hints-controls">
                            <a href="#" class="hints-next" data-tooltip="Next hint"><span class="icon">Next hint</span></a>
                        </span>
                        <span class="hints-text"></span>
                    </div>
                </div>
                <div class="toolbar-split toolbar-split-right">
                    <div id="draft-status"></div>
                </div>
            </div>
             </div> </div>



</div>



<script type="text/x-template" title="dynamic-editor-metadata">
            <meta name="ajs-content-type" content="page">
            <meta name="ajs-min-editor-height" content="150">
            <meta name="ajs-editor-plugin-resource-prefix" content="/s/en_GB-1988229788/4224/875a2723d3ca93f267db5c35cdbfcf91f5910d2d.23/5.1.2/_">
            <meta name="ajs-num-attachments" content="8">
            <meta name="ajs-auto-start" content="false">
            <meta name="ajs-cancel-button-close-text" content="Close">
            <meta name="ajs-content-id" content="58582949">
            <meta name="ajs-action-locale" content="en_GB">
            <meta name="ajs-save-drafts" content="true">
            <meta name="ajs-use-inline-tasks" content="true">
            <meta name="ajs-heartbeat" content="true">
            <meta name="ajs-cancel-button-discard-text" content="">
            <meta name="ajs-draft-id" content="0">
            <meta name="ajs-new-page" content="false">
            <meta name="ajs-form-name" content="inlinecommentform">
            <meta name="ajs-attachment-source-content-id" content="58582949">
            <meta name="ajs-editor-mode" content="richtext">
            <meta name="ajs-draft-type" content="page">
            <meta name="ajs-existing-draft-id" content="0">
            <meta name="ajs-can-attach-files" content="true">

            		    <meta name="ajs-max-thumb-width" content="300">
		    <meta name="ajs-can-send-email" content="true">
		    <meta name="ajs-is-dev-mode" content="false">
		    <meta name="ajs-draft-save-interval" content="30000">
		    <meta name="ajs-show-hidden-user-macros" content="false">
		    <meta name="ajs-is-admin" content="false">
		    <meta name="ajs-confluence.prefs.editor.disable.autocomplete" content="false">
		    <meta name="ajs-confluence.prefs.editor.disable.autoformat" content="false">
		    <meta name="ajs-heartbeat-interval" content="30000">

    </script>


<div id="hidden-permission-fields" class="hidden">
    <input id="viewPermissionsUsers" type="text" name="viewPermissionsUsers" value="">
    <input id="editPermissionsUsers" type="text" name="editPermissionsUsers" value="">
    <input id="viewPermissionsGroups" type="text" name="viewPermissionsGroups" value="">
    <input id="editPermissionsGroups" type="text" name="editPermissionsGroups" value="">
</div>

<script type="text/x-template" title="tableForm">
    <form id="tinymce-table-form" class="aui">
        <div class="field-group">
            <label for="rows">Rows</label>
            <input id="rows" name="rows" type="text" size="3" autocomplete="off" value="{0}">
        </div>
        <div class="field-group">
            <label for="cols">Columns</label>
            <input id="cols" name="cols" type="text" size="3" autocomplete="off" value="{1}">
        </div>
        <div class="field-group hidden">
            <input id="width" type="hidden" name="width" value="">
            <label for="width">Width</label>
        </div>
        <div class="group">
            <div class="checkbox">
                <input id="table-heading-checkbox" class="checkbox" type="checkbox" name="heading" checked="checked" value="true">
                <label for="table-heading-checkbox">First row is heading</label>
            </div>
        </div>
        <div class="group hidden">
            <div class="checkbox">
                <input id="table-equal-width-columns-checkbox" class="checkbox" type="checkbox" name="equal-width-columns" value="false">
                <label for="table-equal-width-columns-checkbox">Equal width columns</label>
            </div>
        </div>
    </form>
</script>
<input type="hidden" name="draftId" value="0" id="draftId"><input type="hidden" name="originalVersion" value="1" id="originalVersion">    <input type="hidden" name="atl_token" value="dfffda9cbc483e2c91bf2838d86b794acc8de2da">
</div>
</body></html>
""")

files = os.listdir('.')

# 首先处理文本
for f in files:
    if f.lower().endswith('.txt'):
        fp = open(f)
        content = fp.read()
        fp.close()
        html.write("<p>%s</p>" % content)

# 然后处理图片
for f in files:
    if f.lower().endswith('.jpg') or f.lower().endswith('.png'):
        html.write("<img src='%s' />" % f)

html.write('</body></html>')
html.close()