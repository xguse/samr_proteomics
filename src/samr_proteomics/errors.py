#!/usr/bin/env python
"""Provide error classes for samr_proteomics."""

# Imports


# Metadata
__author__ = "Gus Dunn"
__email__ = "w.gus.dunn@gmail.com"




class Samr_proteomicsError(Exception):

    """Base error class for samr_proteomics."""


class ValidationError(Samr_proteomicsError):

    """Raise when a validation/sanity check comes back with unexpected value."""
