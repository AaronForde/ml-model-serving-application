#creating an amazon ecr repository for docker image
resource "aws_ecr_repository" "ml-image-repo" {
  name                 = "ml-image-repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

