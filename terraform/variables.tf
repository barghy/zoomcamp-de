variable "gcp_project" {
  description = "Project Name for Google Cloud Resources"
  default     = "zoomcamp-de-410214"
}

variable "gcp_region" {
  description = "Region for Google Cloud Resources"
  default     = "europe-west2"
}

variable "gcp_location" {
  description = "Project Location for Google Cloud Resources"
  default     = "EU"
}

variable "gcs_bucket_name" {
  description = "Bucket Name for Google Cloud Storage"
  default     = "zoomcamp-de-410214-storage"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class for Google Cloud Storage"
  default     = "STANDARD"
}

variable "bq_dataset_name" {
  description = "Dataset Name for Google Big Query"
  default     = "zoomcamp"
}
