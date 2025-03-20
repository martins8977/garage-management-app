<template>
  <q-expansion-item :label="engine.typeEngineName" expand-separator>
    <q-card flat class="q-pa-sm">
      <!-- Exibe os detalhes do engine type -->
      <q-card-section>
        <div><strong>Vehicle ID:</strong> {{ engine.vehicleId }}</div>
        <div><strong>Manufacturer Name:</strong> {{ engine.manufacturerName }}</div>
        <div><strong>Model Name:</strong> {{ engine.modelName }}</div>
        <div>
          <strong>Construção:</strong>
          {{ engine.constructionIntervalStart }} - {{ engine.constructionIntervalEnd }}
        </div>
        <div><strong>Potência (kW):</strong> {{ engine.powerKw }}</div>
        <div><strong>Potência (PS):</strong> {{ engine.powerPs }}</div>
        <div><strong>Combustível:</strong> {{ engine.fuelType }}</div>
        <div><strong>Motor Codes:</strong> {{ engine.engineCodes }}</div>
        <!-- Outros campos podem ser adicionados conforme necessário -->
      </q-card-section>
      <!-- Lista as subcategorias de peças para esse engine type -->
      <q-card-section>
        <q-list>
          <q-item
            v-for="sub in subcategories"
            :key="sub.id"
            clickable
            @click="goToArticles(sub.id)"
          >
            <q-item-section>{{ sub.label }}</q-item-section>
            <q-item-section side>
              <q-btn label="Ver Artigos" color="primary" flat />
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>
  </q-expansion-item>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const props = defineProps({
  engine: { type: Object, required: true },
  manufacturerId: { type: Number, required: true }
})

const router = useRouter()
const subcategories = ref([])

async function fetchSubcategories() {
  try {
    // Chamamos o endpoint Category Variant 2 para buscar subcategorias para o engine type
    // Usamos o vehicleId do engine e o manufacturerId passado como prop
    const response = await axios.get(
      `http://localhost:8000/tecdoc/category-v2/${props.engine.vehicleId}/${props.manufacturerId}`
    )
    console.log("Subcategorias para engine", props.engine.vehicleId, response.data)
    // Supondo que a resposta retorne um objeto com a chave "categories" que seja um array
    if (response.data && response.data.categories) {
      subcategories.value = response.data.categories.map(item => ({
        id: item.levelId_2,
        label: item.levelText_2 || 'Sem nome'
      }))
    } else {
      subcategories.value = []
    }
  } catch (error) {
    console.error("Erro ao buscar subcategorias:", error)
  }
}

function goToArticles(subcatId) {
  if (!subcatId) return
  // Navega para a página de artigos usando a rota definida: /articles/:manufacturerId/:vehicleId/:subCategoryId
  router.push(`/articles/${props.manufacturerId}/${props.engine.vehicleId}/${subcatId}`)
}

onMounted(() => {
  fetchSubcategories()
})
</script>
