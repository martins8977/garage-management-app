<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">
      Veículos do Cliente: {{ clientId }}
    </div>

    <!-- Botão para abrir o formulário de novo veículo -->
    <q-btn label="Adicionar Novo Veículo" color="primary" @click="showDialog = true" />

    <!-- Diálogo com o formulário para adicionar veículo -->
    <q-dialog v-model="showDialog" persistent>
      <q-card style="min-width: 400px">
        <q-card-section>
          <div class="text-h6">Novo Veículo</div>
        </q-card-section>

        <q-card-section>
          <q-form @submit.prevent="submitNewVehicle" class="q-gutter-md">
            <!-- Matrícula -->
            <q-input filled v-model="form.licensePlate" label="Matrícula" required />

            <!-- Seleção da Marca -->
            <q-select
              filled
              v-model="form.manufacturerId"
              label="Marca"
              :options="brands"
              option-label="brand"
              option-value="manufacturerId"
              emit-value
              @update:model-value="onBrandChange"
              required
            />

            <!-- Seleção do Modelo -->
            <q-select
              filled
              v-model="form.modelId"
              label="Modelo"
              :options="models"
              option-label="modelName"
              option-value="modelId"
              emit-value
              @update:model-value="onModelChange"
              required
            />

            <!-- Seleção do Tipo de Motor -->
            <q-select
              filled
              v-model="form.vehicleTypeId"
              label="Tipo de Motor"
              :options="engineTypes"
              option-label="typeEngineName"
              option-value="vehicleId"
              required
            />

            <!-- Ano -->
            <q-input filled v-model="form.year" label="Ano" type="number" required />
          </q-form>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancelar" v-close-popup />
          <q-btn label="Salvar" color="primary" @click="submitNewVehicle" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
// Supõe que o clientId vem como parâmetro de rota, ex: /new-vehicle/:clientId
const clientId = route.params.clientId

// Controle do diálogo
const showDialog = ref(false)

// Objeto que armazenará os dados do novo veículo
const form = ref({
  licensePlate: '',
  manufacturerId: null,
  modelId: null,
  vehicleTypeId: null,
  year: null,
  clientId: clientId,
})

// Arrays para os dados carregados via API TecDoc
const brands = ref([])
const models = ref([])
const engineTypes = ref([])

// Carregar as marcas ao montar a página
onMounted(async () => {
  try {
    // Exemplo de endpoint para obter as marcas (ajuste conforme a tua resposta)
    const response = await axios.get('http://localhost:8000/tecdoc/all-brands-debug')
    // Se a resposta tiver uma chave "manufacturers", usa-a; senão, assume que a resposta é um array
    brands.value = response.data.manufacturers || response.data
  } catch (error) {
    console.error('Erro ao carregar marcas:', error)
  }
})

// Quando o usuário selecionar uma marca, carrega os modelos dessa marca
async function onBrandChange(selectedManufacturerId) {
  form.value.modelId = null
  form.value.vehicleTypeId = null
  models.value = []
  engineTypes.value = []
  try {
    const response = await axios.get(`http://localhost:8000/tecdoc/models/${selectedManufacturerId}`)
    models.value = response.data.models || []
  } catch (error) {
    console.error('Erro ao carregar modelos:', error)
  }
}

// Quando o usuário selecionar um modelo, carrega os tipos de motor desse modelo
async function onModelChange(selectedModelId) {
  form.value.vehicleTypeId = null
  engineTypes.value = []
  try {
    const response = await axios.get(`http://localhost:8000/tecdoc/engine-types/${form.value.manufacturerId}/${selectedModelId}`)
    engineTypes.value = response.data.modelTypes || []
  } catch (error) {
    console.error('Erro ao carregar tipos de motor:', error)
  }
}

// Função para enviar o formulário e criar o veículo
async function submitNewVehicle() {
  try {
    // Procura o objeto de marca e modelo para obter as strings
    const selectedBrandObj = brands.value.find(b => b.manufacturerId === form.value.manufacturerId)
    const selectedModelObj = models.value.find(m => m.modelId === form.value.modelId)

    // Prepara o payload com os nomes de campos corretos
    const payload = {
      license_plate: form.value.licensePlate,
      brand: selectedBrandObj ? selectedBrandObj.brand : "",
      model: selectedModelObj ? selectedModelObj.modelName : "",
      year: form.value.year,
      customer_id: 2,
    }
    const response = await axios.post('http://localhost:8000/vehicles', payload)
    console.log('Veículo criado com sucesso:', response.data)
    showDialog.value = false
    // Redireciona para a página de veículos do cliente, se existir
    router.push(`/clients/${clientId}/vehicles`)
  } catch (error) {
    console.error('Erro ao criar veículo:', error)
  }
}
</script>
