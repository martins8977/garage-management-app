<template>
  <q-expansion-item :label="engine.typeEngineName" expand-separator>
    <q-select
      v-model="selectedSubcategory"
      :options="subcategoryOptions"
      option-label="label"
      option-value="id"
      emit-value
      filled
      label="Selecione uma subcategoria"
    />
    <q-btn
      label="Ver Artigos"
      color="primary"
      @click="goToArticles"
      :disable="!selectedSubcategory"
    />
  </q-expansion-item>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const props = defineProps({
  engine: {
    type: Object,
    required: true
  }
})

const router = useRouter()
const selectedSubcategory = ref(null)
const subcategoryOptions = ref([])

async function fetchSubcategories() {
  console.log('engine:', props.engine)
  try {
    const response = await axios.get(
      `http://localhost:8000/tecdoc/category-v2/${props.engine.vehicleId}/${props.engine.manufacturerId}`
    )
    console.log("Subcategorias:", response.data)
    if (response.data && response.data.categories) {
      subcategoryOptions.value = response.data.categories.map(item => ({
        id: item.levelId_2,
        label: item.levelText_2 || 'Sem nome'
      }))
    } else {
      subcategoryOptions.value = []
    }
  } catch (error) {
    console.error("Erro ao buscar subcategorias", error)
  }
}

function goToArticles() {
  if (!selectedSubcategory.value) return
  router.push(`/articles/${props.engine.manufacturerId}/${props.engine.vehicleId}/${selectedSubcategory.value}`)
}

onMounted(() => {
  fetchSubcategories()
})
</script>
