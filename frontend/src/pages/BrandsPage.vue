<template>
  <q-page class="q-pa-md">
    <div class="text-h5">Marcas Obtidas da TecDoc</div>
    <q-table
      :rows="brands"
      :columns="columns"
      row-key="manufacturerId"
      flat
      bordered
      separator="horizontal"
    >
      <template v-slot:body-cell-actions="props">
        <q-td :props="props">
          <q-btn
            color="primary"
            label="Ver Modelos"
            @click="goToModels(props.row.manufacturerId)"
          />
        </q-td>
      </template>
    </q-table>
    <q-banner v-if="brands.length === 0" class="q-mt-md" dense>
      Não foram encontradas marcas.
    </q-banner>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const brands = ref([])
const columns = [
  { name: 'manufacturerId', label: 'ID', field: 'manufacturerId', align: 'left', sortable: true },
  { name: 'brand', label: 'Marca', field: 'brand', align: 'left', sortable: true },
  { name: 'actions', label: 'Ações', field: 'actions', align: 'center' }
]

async function fetchBrands() {
  try {
    const response = await axios.get('http://localhost:8000/tecdoc/all-brands-debug')
    // Se a resposta tiver a chave "manufacturers":
    if (response.data && response.data.manufacturers) {
      brands.value = response.data.manufacturers
    } else {
      brands.value = []
    }
  } catch (error) {
    console.error("Erro ao carregar as marcas:", error)
  }
}

function goToModels(manufacturerId) {
  router.push(`/models/${manufacturerId}`)
}

onMounted(() => {
  fetchBrands()
})
</script>
