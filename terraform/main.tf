terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.10.0"
    }
  }
}

provider "google" {
  credentials = file("../.google/credentials/google_credentials.json")
  project     = var.gcp_project
  region      = var.gcp_region
}

resource "google_storage_bucket" "zoomcamp-de-storage" {
  name          = var.gcs_bucket_name
  location      = var.gcp_location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "zoomcamp-de-warehouse" {
  dataset_id = var.bq_dataset_name
  location   = var.gcp_location
}