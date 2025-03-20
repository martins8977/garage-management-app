<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">
      Categorias de Peças (Variant 3)
    </div>

    <q-table
      :rows="categories"
      :columns="columns"
      row-key="categoryId"
      flat
      bordered
      separator="horizontal"
    >
      <template v-slot:body-cell-categoryName="props">
        <q-td :props="props">
          {{ props.row.categoryName }}
        </q-td>
      </template>
      <template v-slot:body-cell-actions="props">
        <q-td :props="props">
          <q-btn label="Ver Subcategorias" color="primary" @click="goToSubCategories(props.row.categoryId)" />
        </q-td>
      </template>
    </q-table>

    <q-banner v-if="categories.length === 0" class="q-mt-md" dense>
      Nenhuma categoria encontrada.
    </q-banner>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

// Recebe o manufacturerId da rota, ex: /categories/121
const route = useRoute()
const router = useRouter()
const manufacturerId = ref(route.params.manufacturerId || 0)

// Usamos um valor fixo para category_id para Variant 3, conforme exemplo (ex: 19942)
const categoryIdParam = 19942

const categories = ref([])

// Definir as colunas para a QTable
const columns = [
  { name: 'categoryId', label: 'ID', field: 'categoryId', align: 'left', sortable: true },
  { name: 'categoryName', label: 'Categoria', field: 'categoryName', align: 'left', sortable: true },
  { name: 'actions', label: 'Ações', field: 'actions', align: 'center' }
]

// Função para buscar as categorias via backend
async function fetchCategories() {
  try {
    // Chama o endpoint Variant 3: /tecdoc/category-v3/{categoryIdParam}/{manufacturerId}
    const response = await axios.get(`http://localhost:8000/tecdoc/category-v3/${categoryIdParam}/${manufacturerId.value}`)
    console.log('Resposta Category Variant 3:', response.data)
    // Supondo que a resposta tenha uma chave "categories" que é um array
    if (response.data && response.data.categories) {
      categories.value = response.data.categories
    } else {
      categories.value = []
    }
  } catch (error) {
    console.error('Erro ao carregar categorias:', error)
  }
}

// Função para navegar para a página de subcategorias (Category Variant 1)
function goToSubCategories(selectedCategoryId) {
  // Navega para uma nova rota, por exemplo, /subcategories/:manufacturerId/:categoryId
  router.push(`/subcategories/${manufacturerId.value}/${selectedCategoryId}`)
}

onMounted(() => {
  fetchCategories()
})
</script>
