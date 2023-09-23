# An Introduction to Server Configuration Management


## Puppet manifests

Benefits of Configuration Management for Servers

To name a few:
*** Quick Provisioning of New Servers ***

Whenever a new server needs to be deployed, a configuration management tool can automate most, if not all, of the provisioning process for you. Manually deploying a web server, for instance, could take hours compared to a few minutes with configuration management/automation.

*** Quick Recovery from Critical Events ***

When a server goes offline due to unknown circumstances, deploying a replacement server is usually the safest way to get your services back online while a detailed inspection is done on the affected server. With configuration management and automation, this can be done in a quick and reliable way.

*** No More Snowflake Servers ***

With time, it may become extremely difficult to know exactly what is installed on a server and which changes were made. By using a configuration management tool, the procedure necessary for bringing up a new server or updating an existing one will be all documented in the provisioning scripts.

*** Version Control for the Server Environment ***

Once you have your server setup translated into a set of provisioning scripts,
Version control tools, such as Git, can be used to keep track of changes made to the provisioning and to maintain separate branches for legacy versions of the scripts. You can also use version control to implement a code review policy for the provisioning scripts. This practice will add extra consistency to your infrastructure setup.

*** Replicated Environments ***
<img=https://github.com/viictoo/alx-system_engineering-devops/blob/master/0x0A-configuration_management/resources/puppeteer.jpg>
Configuration management makes it trivial to replicate environments with the exact same software and configurations. This enables you to effectively build a multistage ecosystem, with production, development, and testing servers. This practice will minimize problems caused by environment discrepancies that frequently occur when applications are deployed to production or shared between co-workers with different machine setups (different operating system, software versions and/or configurations).

 	Ansible 	Puppet 	Chef
Script Language 	YAML 	Custom DSL based on Ruby 	Ruby
Infrastructure 	Controller machine applies configuration on nodes via SSH 	Puppet Master synchronizes configuration on Puppet Nodes 	Chef Workstations push configuration to Chef Server, from which the Chef Nodes will be updated
Requires specialized software for nodes 	No 	Yes 	Yes
Provides centralized point of control 	No. Any computer can be a controller 	Yes, via Puppet Master 	Yes, via Chef Server
Script Terminology 	Playbook / Roles 	Manifests / Modules 	Recipes / Cookbooks
Task Execution Order 	Sequential 	Non-Sequential 	Sequential


Links:
https://www.puppet.com/docs/puppet/5.5/types/file.html#file-attribute-ensure
https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management#overview-of-configuration-management-tools
http://puppet-lint.com/

 Installs::

Install puppet
```
 apt-get install -y ruby=1:2.7+1 --allow-downgrades
 apt-get install -y ruby-augeas
 apt-get install -y ruby-shadow
 apt-get install -y puppet
```

Install puppet-lint
```
 gem install puppet-lint
```
