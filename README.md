# Sitecheck

This is a Pythonista 3 script/app for checking web sites.

## Description

### Site

Type the web URL into this text field.  Should begin with `http://` or `https://`.

### Headers

Here is where you can set headers for your request, such as a "Host" header.  In the left column you type the name of the header, such as `Host`.  In the right column you type the value that you are setting for that header, such as `www.github.com`.

Right now you only have the option of setting a single header.  Once I get more time I may make it a bit more dynamic.

### Follow Redirects

When enabled, the process will follow any redirects that it receives in the response.  When disabled, it will not follow the redirects.

## Viewing Results

### HeaderView

In the top bordered box, you will see the headers in your response.

### WebView

In the bottom bordered box, you will see the rendered HTML that was returned in your response (if there is any).
