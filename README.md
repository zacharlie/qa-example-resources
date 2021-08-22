# Example Resources

This repository comprises a variety of QGIS shareable resources for demonstrating the functionality of the [Quality Assurance Workbench](https://github.com/kartoza/qgis_dataset_qa_workbench) QGIS Plugin and providing a template for users to learn and start building their own checklists.

## About The QA Workbench

This plugin allows loading checklists with designated steps, allowing users to design workflows for the management of process.

Each checklist step is intended to have some form of verification, but steps are customisable and provides various fields, including instructional information or the capture of generic note taking.

Checklists are simple JSON documents with a predefined schema. Checklist steps are integrated with the QGIS Processing Framework which allows processing and verification steps to adopt a semi-automatic workflow structure.

In addition, the plugin provides interfaces for the development of reports which may be stored as pdfs, emailed to other agents as part of approval workflows, or attached to layer metadata in QGIS to facilitate data integrity and provenance preservation.

## About QGIS Resource Sharing

This is a resources repository designed to be utilised with the [QGIS Resource Sharing Plugin](http://qgis-contribution.github.io/QGIS-ResourceSharing/).

The resource sharing plugin provides a simple method for the distribution and utilisation of assets and resources that may be used within QGIS, including custom symbols, processing algorithms, models, processing checklists and more.

## Resources

The repository contains only a single collection, example-resources. The resource sharing collection structure does support multiple collections, however additional collections are not required at this time.

The shared resources include a single SVG for demo purposes, processing models and processing scripts used in QA workflows, and checklists which demonstrate basic and common functionalities for the QA Workbench plugin.

## Installing the Resource Sharing Plugin

Using the QGIS Resource Sharing Plugin was demonstrated in the [QGIS Open Day - Touring the QGIS model builder](https://www.youtube.com/watch?v=w6Z2bDfDIxw&t=2537s) session.

In QGIS Desktop, open the plugins menu and search for *QGIS Resource Sharing* under all plugins. Click install on the interface to install the plugin for the currently active user profile.

![qgis plugins menu](https://user-images.githubusercontent.com/64078329/96585422-e0980c00-12df-11eb-8252-d84d5bbda4ac.png)

Once the plugin is installed, the plugin is available from the QGIS Toolbar, or from the plugin menu under *Resource Sharing*.

![qgis resource sharing toolbar](https://user-images.githubusercontent.com/64078329/96585653-2ead0f80-12e0-11eb-8be0-4cb9c6ea4874.png)

Clicking on the icon will bring up the main interface. To install the relevant resources, simply select your repository and select *install*.

![qgis resource sharing ui](https://user-images.githubusercontent.com/64078329/96596456-04ae1a00-12ed-11eb-9de5-1fc951dfbee7.png)

**The assets should be available automatically from their relevant controller elements once the repository is installed.**

Custom processing models, scripts and algorithms may be accessed via the processing menu items and used in the same manner as native processing utilities.

![custom processing elements](https://user-images.githubusercontent.com/64078329/129926383-fa366aeb-5920-4408-894e-b5d275c4c0b8.png)

In the case of SVGs, this will enable the images to be accessed from the SVG elements menus.

![svg resources](https://user-images.githubusercontent.com/64078329/96596521-1abbda80-12ed-11eb-9384-6663352f003c.png)

## Adding the remote repository

Custom repositories are not available by default and will need to be explicitly added for all relevant QGIS user profiles. To add the repository, open the QGIS Resource Sharing plugin and navigate to the *Settings* tab. Click the *Add repository* button and input the preferred name for your repository, such as `QA Example`, along with the URL to the remote repository, followed by the *.git* extension, e.g. `https://github.com/zacharlie/qa-example-resources.git`.

![Add Repository UI](https://user-images.githubusercontent.com/64078329/96613217-f963ea00-12fe-11eb-8ae8-b4fd9df2dd2b.png)

## Adding a local repository

Users may create, clone or download a compatible repository or structure one in accordance with the QGIS Resource Plugin Documentation. Users that are unfamiliar with git are encouraged to make use of GitHub desktop and make a clone of this repository to their local environment.

- Windows/ Mac: https://desktop.github.com/
- Linux: https://github.com/shiftkey/desktop

Once the repository is available, it may be added to the plugin by using the relevant syntax for the filepath, as indicated in the table below:
|System|Syntax|
|:-----|:-----|
|Windows Local|`file:d:\path\qgis-resources.git`|
|Network Share|`file:\\servername\share\qgis-resources.git`|
|MAC/Linux System|`file:/home/user/path/qgis-resources.git`|
|MAC/Linux Userspace|`file:~/path/qgis-resources.git`|

## Updating a repository

The resource sharing plugin allows users to update or uninstall the resources shared via the plugin via the plugin interface. Before updating a local repository, a user will need to update the local repository with the remote source before performing the updates in the plugin interface. This is possible via the GitHub desktop interface using the "Fetch Origin" command.

![Fetch origin](https://user-images.githubusercontent.com/64078329/97091008-de63e380-1638-11eb-8641-d57d2ec71af7.png)

## Checklists

The following table outlines the available checklists and their associated functionality/ purpose.

<!-- Use HTML table because large md tables aren't really readable -->
<table>
  <thead>
    <tr>
      <th>Checklist</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>example.checklist</td>
      <td>
        Sample checklist demonstrating the simplest checklist structure.
        Note how the checklist is recognised by the plugin despite not having a json file extension.
      </td>
    </tr>
    <tr>
      <td>invalid-checklist.json</td>
      <td>
        Sample checklist demonstrating an invalid checklist structure.
        If checklists cannot be validated by the JSON Schema definition, they are not recognised by the plugin.
      </td>
    </tr>
    <tr>
      <td>archive-project</td>
      <td>
        Checklist for ensuring correct procedure is followed for archiving a project
      </td>
    </tr>
    <tr>
      <td>create-project</td>
      <td>
        Checklist for ensuring correct procedure is followed for creating a new project
      </td>
    </tr>
    <tr>
      <td>generic-raster-dataset-import</td>
      <td>Import raster layers into the Geoserver instance</td>
    </tr>
    <tr>
      <td>generic-vector-dataset-import</td>
      <td>Import vector layers into the GIS database</td>
    </tr>
    <tr>
      <td>vector-data-preliminary-publication</td>
      <td>Publication workflow for initial and internal vector data</td>
    </tr>
    <tr>
      <td>vector-data-validated-publication</td>
      <td>Publication workflow for validated and published vector data</td>
    </tr>
    <tr>
      <td>raster-data-validated-publication</td>
      <td>Publication workflow for validated and published raster data</td>
    </tr>
  </tbody>
</table>
