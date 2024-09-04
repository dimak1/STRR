<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    header: string
    showRemoveButton: boolean
  }>(),
  {
    showRemoveButton: false
  }
)

const emit = defineEmits(['removeCard'])

const { t } = useTranslation()
</script>

<template>
  <div class="bg-white">
    <div class="bg-bcGovColor-gray2 rounded-t-[4px] h-14 items-center flex px-10 justify-between">
      <h3 class="font-bold">
        {{ props.header }}
      </h3>

      <BcrosButtonsPrimary
        v-if="showRemoveButton"
        :action="() => emit('removeCard')"
        :label="t('common.removeButton')"
        class-name="px-0 py-1 mobile:grow-0"
        variant="ghost"
        :icon="'i-mdi-remove'"
        trailing
      />
    </div>
    <div class="">
      <slot name="default" />
    </div>
  </div>
</template>

<style scoped></style>
