<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">
      Artigos para Vehicle ID: {{ vehicleId }}, Subcategoria: {{ subCategoryId }}, Marca: {{ manufacturerId }}
    </div>
    <q-table
      :rows="articles"
      :columns="columns"
      row-key="articleId"
      flat
      bordered
      separator="horizontal"
    >
      <!-- Exemplo de template customizado para coluna de Número do Artigo -->
      <template v-slot:body-cell-articleNo="props">
        <q-td :props="props">
          {{ props.row.articleNo }}
        </q-td>
      </template>
      <!-- Para o nome do produto -->
      <template v-slot:body-cell-articleProductName="props">
        <q-td :props="props">
          {{ props.row.articleProductName }}
        </q-td>
      </template>
      <!-- Para o fornecedor -->
      <template v-slot:body-cell-supplierName="props">
        <q-td :props="props">
          {{ props.row.supplierName }}
        </q-td>
      </template>
      <!-- Para a imagem (se disponível) -->
      <template v-slot:body-cell-imageLink="props">
        <q-td :props="props">
          <img :src="props.row.imageLink" alt="Artigo" style="max-width: 80px;" />
        </q-td>
      </template>
    </q-table>
    <q-banner v-if="articles.length === 0" class="q-mt-md" dense>
      Nenhum artigo encontrado.
    </q-banner>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const manufacturerId = ref(Number(route.params.manufacturerId))
const vehicleId = ref(Number(route.params.vehicleId))
const subCategoryId = ref(Number(route.params.subCategoryId))
const articles = ref([])

const columns = [
  { name: 'articleId', label: 'ID', field: 'articleId', align: 'left', sortable: true },
  { name: 'articleNo', label: 'Número', field: 'articleNo', align: 'left', sortable: true },
  { name: 'articleProductName', label: 'Nome do Produto', field: 'articleProductName', align: 'left', sortable: true },
  { name: 'supplierName', label: 'Fornecedor', field: 'supplierName', align: 'left', sortable: true },
  { name: 'imageLink', label: 'Imagem', field: 'imageLink', align: 'center' }
]

async function fetchArticles() {
  try {
    const url = `http://localhost:8000/tecdoc/articles/${vehicleId.value}/${subCategoryId.value}/${manufacturerId.value}`
    console.log("Chamando URL:", url)
    const response = await axios.get(url)
    console.log("Artigos retornados:", response.data)
    if (Array.isArray(response.data)) {
      articles.value = response.data
    } else if (response.data && response.data.articles) {
      articles.value = response.data.articles
    } else {
      articles.value = []
    }
  } catch (error) {
    console.error("Erro ao carregar artigos:", error)
  }
}

onMounted(() => {
  fetchArticles()
})
</script>
