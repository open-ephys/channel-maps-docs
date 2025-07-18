.. _guide:

==============================
User Guide
==============================

What information is included in each page
=================================================

These docs provide physical specifications of the headstages, adapters and electrode interface boards (EIBs) produced by Open Ephys.
We provide channel maps of headstages and adapter/EIB combinations in which channels are labelled on an image of the physical pins in the order in which they appear in software order to help users extend the channel maps to probes or electrodes, reducing the need to interpret schematics or tables.

In each device page we include:

- General characteristics such as weight and dimensions, connector part numbers and REF and GND connections, among others.

- Channel maps:

  - For headstages, the channel mapping is an image showing the physical location of the channels on the headstage.

  - When adapters or EIBs compatible with that headstage exist, we have included the connection orientation and channel mapping for each combination.

.. - For adapters and EIBs, we have included the pinout of which connector pins connect to which vias or pins. 

- Additional sensor physical specifications such as accelerometer or inertial measurement unit orientation axes.

- Tables detailing the connector pinouts for creating other channel maps, including pinout labelled images. 

Important considerations
==============================

We have provided the channel numbering in the order in which channels appear in software. These correspond to the bioamplifier chip channel numbering (Intan chip), which starts at 0. These channel numbers that relate to a software or sensor reference numbering are written in black on the images.

In Bonsai, the channel numbering starts at 0.
In the Open Ephys GUI, the channel numbering starts at 1. When using the Open Ephys GUI, make sure you add 1 to the channel numberings provided in this documentation.

Where connector pinouts are presented, the labels are attributed to pins based on connector or schematics part numbering. The pin numbers are written in red on the images.

More resources about channel mapping
=========================================

We suggest using the `ProbeInterface <https://probeinterface.readthedocs.io/>`__ Python library to help finish the mapping from the headstage/adapter/EIB to the electrodes.

.. - Open Ephys Community Wiki article on channel mapping
.. - OEdu video on channel mapping
