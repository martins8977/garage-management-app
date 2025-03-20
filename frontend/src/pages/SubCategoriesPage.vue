<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">
      Subcategorias para o Veículo ID: {{ vehicleId }} da Marca: {{ manufacturerId }}
    </div>

    <q-list>
      <q-expansion-item
        v-for="group in groupedCategories"
        :key="group.label"
        :label="group.label"
        expand-separator
      >
        <q-list>
          <q-item
            v-for="subcat in group.children"
            :key="subcat.id"
            clickable
            @click="goToArticles(subcat.id)"
          >
            <q-item-section>{{ subcat.label }}</q-item-section>
          </q-item>
        </q-list>
      </q-expansion-item>
    </q-list>

    <q-banner v-if="groupedCategories.length === 0" class="q-mt-md" dense>
      Nenhuma subcategoria encontrada.
    </q-banner>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()

const manufacturerId = ref(route.params.manufacturerId)
const vehicleId = ref(route.params.vehicleId)

const groupedCategories = ref([])

onMounted(async () => {
  try {
    const response = await axios.get(`http://localhost:8000/tecdoc/category-v1/${vehicleId.value}/${manufacturerId.value}`)
    console.log('Resposta Category Variant 1:', response.data)
    if (response.data && response.data.categories) {
      // Se a resposta for um objeto, converte-o em array
      const catArray = []
      for (const key in response.data.categories) {
        if (Object.hasOwn(response.data.categories, key)) {
          catArray.push(response.data.categories[key])
        }
      }
      groupedCategories.value = groupByLevelText1(catArray)
    }
  } catch (error) {
    console.error('Erro ao carregar subcategorias:', error)
  }
})

function groupByLevelText1(catArray) {
  const map = {}
  catArray.forEach(item => {
    const mainLabel = item.levelText_1 || 'Sem nome'
    if (!map[mainLabel]) {
      map[mainLabel] = []
    }
    if (item.levelId_2) {
      map[mainLabel].push({
        id: item.levelId_2,
        label: item.levelText_2 || 'Sem nome'
      })
    }
  })
  const result = []
  for (const key in map) {
    result.push({
      label: key,
      children: map[key]
    })
  }
  return result
}

function goToArticles(subcatId) {
  if (!subcatId) return
  router.push(`/articles/${manufacturerId.value}/${vehicleId.value}/${subcatId}`)
}
</script>
