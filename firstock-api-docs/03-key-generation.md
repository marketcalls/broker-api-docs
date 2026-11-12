# Key Generation

> Source: https://firstock.in/api/docs/key-generation/

> This page guides you to generate the API key and Vendor code to login into Firstock Developer API.

> This IP whitelisting process has been implemented in accordance with **SEBI’s latest security guidelines**, which will become **mandatory from April 1, 2026**.

## Overview

API keys are required to authenticate your login requests to the Firstock platform. Additionally, IP whitelisting ensures that API access is restricted only to trusted IP addresses .By following the steps below, you will generate a secure API key, whitelist your IP, and be ready to integrate Firstock’s trading and market data services into your application.

## Why You Need an API Key

1. Authentication: An API key uniquely identifies you when you interact with Firstock APIs.
2. Access Control: Generates jkey (susertoken) which helps in certain operations (e.g., placing trades, retrieving account details).

## **Why IP Whitelisting is Required**

1. **Enhanced Security**: Ensures that only approved IP addresses can access the APIs .
2. **Regulatory Compliance**: Mandatory as per SEBI guidelines .
3. **Access Restriction**: Prevents unauthorized systems from making API requests

## Prerequisites

1. Account Access: Ensure you have account access to generate API keys on [key generation platform](https://firstock.in/api/?ref=firstock.in).
2. Key Management Section: Familiarize yourself with the portal or tool where keys can be created (e.g., “API Keys,” “Profile,” and “Docs” sections in your dashboard).

## Steps to Generate an API Key

**1.Navigate to Key Generation**

- First, log in to the key generation portal on the provided [Key Generation](https://firstock.in/api/?ref=firstock.in).

![loginscreen1.png](https://firstock.in/api/docs/content/images/2025/09/loginscreen1.png)

**2. Generate a New Key**

- In your dashboard, locate the API Keys.
- Click on the button or link to Generate Key or Create New Key.
- The appkey and vendor code will be generated

![apikeyscreen.png](https://firstock.in/api/docs/content/images/2025/09/apikeyscreen-1.png)

**3.Securely Store Your Key**

1. After generation, your API Key (and Secret Key, if applicable) will be shown.

**Important**: The key will expire after 365 days and a new key has to be generated.

## **Steps to Whitelist Your IP Address**

1. Click on the **“Add IP”** button
2. Enter your IP address details:

  1. **Primary IP Address** (Mandatory)
  2. **Secondary IP Address** (Optional)
3. A maximum of **two IP addresses** can be whitelisted per account
4. Click on **Submit** to save the changes

## **Updating or Changing IP Address**

1. Click on the **“Delete IP”** option
2. Follow the steps mentioned above to add the new IP address

## Best Practices

1. Protect Your Keys: Never expose your keys in client-side code or in publicly accessible repositories.
2. Use HTTPS: Always send your key over secure HTTP (HTTPS) to prevent interception.
3. Rotate Regularly: Update or regenerate your keys periodically to maintain a higher level of security.
