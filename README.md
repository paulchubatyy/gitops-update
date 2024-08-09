# gitops-update

GitHub Action that updates a single key in another GitHub repository.

## Example:

You have a `kustomization.yaml` file in a `myorg/app-env` repository that has below content:

Add this to GitHub action:

```yaml
- name: GitOps Update
  uses: paulchubatyy/gitops-update@main
  with:
	filename: "path/to/kustomization.yaml"
	key: "images.0.newTag"
	value: "${{ github.sha }}"
	github-deploy-key: ${{ secrets.GITOPS_SSH_PRIVATE_KEY }}
	github-org-and-repo: "myorg/app-env"
```

