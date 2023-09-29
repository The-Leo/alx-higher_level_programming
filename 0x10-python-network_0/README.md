# 0x10. Python - Network #0

## URL

A URL, which stands for Uniform Resource Locator, is a reference or address used to access resources on the internet. It is a string of characters that specifies the location and the method of accessing a resource, typically on the World Wide Web.

## HTTP
HTTP, which stands for Hypertext Transfer Protocol, is a fundamental protocol used for communication on the World Wide Web. It defines the rules and conventions for transmitting and receiving hypertext (text with embedded links) and multimedia elements like images, videos, and other resources over the internet.

# HOW TO READ A URL

To read and understand a URL (Uniform Resource Locator), you need to break it down into its individual components. 

Let's take an example URL: https://www.leonard.com:8080/products/page1?q=term&limit=10#section1

**Scheme:** The scheme indicates the protocol or method used to access the resource. In this example, the scheme is "https." It tells us that Hypertext Transfer Protocol Secure (HTTPS) will be used for communication.

**Domain:** The domain is the human-readable name of the server where the resource is hosted. In this case, the domain is "www.leonard.com." This is the address of the server you are connecting to.

**Port:** The port number (if present) specifies the communication endpoint on the server. In our example, it's "8080." If not specified, the default port for the scheme (e.g., 80 for HTTP, 443 for HTTPS) is used.

**Path:** The path specifies the location of the resource on the server's file system. After the domain, it typically starts with a forward slash ("/"). In our example, the path is "/products/page1," indicating the resource's location on the server.

**Query:** The query component (if present) follows a question mark ("?") and consists of key-value pairs separated by ampersands ("&"). In our URL, the query is "q=term&limit=10," passing parameters "q" with the value "term" and "limit" with the value "10" to the resource.

**Fragment:** The fragment component (if present) starts with a hash symbol ("#"). It specifies a specific section or identifier within the resource. In this case, it's "#section1," indicating a particular section within the webpage.

So, when you read the URL step by step:

Protocol: HTTPS
Domain: www.leonard.com
Port: 8080
Path: /products/page1
Query: ?q=term&limit=10
Fragment: #section1

In this networking project, I used curl in Bash scripts to send various types of HTTP headers. In the process, I learned about how URL's work, domain names, the many different HTTP request/repsonse header fields and status codes, and how to utilize cookies.
