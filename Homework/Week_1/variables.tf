variable "credentials" {
  description = "my credentials"
  default     = "~/.gc/my-creds.json"
}

variable "project" {
  description = "name of project"
  default     = "de-zoomcamp-test"
}

variable "location" {
  description = "project location"
  default     = "EU"
}

variable "region" {
  description = "region location"
  default     = "europe-west2-a"
}

variable "bq_dataset_name" {
  description = "name of the bq data set"
  default     = "jm_dataset_terra_test"
}

variable "gcs_bucket_name" {
  description = "name of the bucket"
  default     = "de-zoomcamp-test-jm-terra-bucket"
}

variable "gcs_storage_class" {
  description = "bucket storage class"
  default     = "STANDARD"
}