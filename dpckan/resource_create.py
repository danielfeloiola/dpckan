import urllib
import json
import pprint
import os
import requests
import json
import collections
import sys
import click
from ckanapi import RemoteCKAN
from dpckan.functions import (os_slash, buscaListaDadosAbertos, buscaDataSet,
                              buscaPastaArquivos, removePastaArquivos,
                              buscaArquivos, atualizaMeta, load_complete_datapackage,
                              resource_update, update_datapackage_json_resource, resource_create,
                              resources_metadata_create)
import ipdb

@click.command()
@click.option('--ckan-host', '-H', envvar='CKAN_HOST', required=True,
              help="Ckan host, exemplo: http://dados.mg.gov.br ou https://dados.mg.gov.br")  # -H para respeitar convenção de -h ser help
@click.option('--ckan-key', '-k', envvar='CKAN_KEY', required=True,
              help="Ckan key autorizando o usuário a realizar publicações/atualizações em datasets")
@click.option('--package-id', '-pi', required=True,
              help="Nome do dataset para qual será incluido o recurso.")
@click.option('--resource-name', '-rn', required=True,
              help="Nome do recurso a ser incluído. Chave 'name' do recurso dentro do arquivo datapackage.json")
def resource_upload(ckan_host, ckan_key, package_id, resource_name):
  # try:
  datapackage_path = f'.{os_slash}datapackage.json'
  package = load_complete_datapackage(datapackage_path)
  # Show package to find datapackage.json resource id
  # Update datapakcage.json resource
  update_datapackage_json_resource(ckan_host, ckan_key, package_id)
  # Create new resource
  print(f"Criando recurso: {resource_name}")
  resource_ckan = resource_create(ckan_host,
                                  ckan_key,
                                  package_id,
                                  package.get_resource(resource_name))
  resources_metadata_create(ckan_host,
                            ckan_key,
                            resource_ckan['id'],
                            package.get_resource(resource_name))

