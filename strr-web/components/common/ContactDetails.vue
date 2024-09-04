<script setup lang="ts">
import FormCard from './FormCard.vue'

const props = withDefaults(
  defineProps<{
    header: string
    state: Record<string, any>
    showAlertMsg: boolean
    showRemoveButton: boolean
  }>(),
  {
    showAlertMsg: false,
    showRemoveButton: false
  }
)

const emit = defineEmits(['removeContactDetails'])

const { userFullName } = useBcrosAccount()
const { t } = useTranslation()
const slots = useSlots()

const hasContactInfoOverride = computed(() => !!slots.contactInfo)

// TODO: Update this
const temp = ref(null)

</script>

<template>
  <FormCard
    :header="props.header"
    class="mb-8"
    :show-remove-button="props.showRemoveButton"
    @removeCard="emit('removeContactDetails')"
  >
    <div class="flex m:flex-col d:p-10 m:p-5">
      <!-- Left Column -->
      <div class="w-[200px]">
        <div class="mb-6 font-bold text-gray-700">
          Contact Details
        </div>
      </div>

      <!-- Right Column -->
      <div class="flex-1 space-y-6">
        <slot v-if="hasContactInfoOverride" name="contactInfo" />

        <div v-else>
          <div class="text-[14px] leading-[22px]">
            {{ t('common.yourName') }}
          </div>
          <div class="mb-[16px] text-[14px] leading-[22px]">
            {{ userFullName }}
          </div>

          <div ref="testRef" class="mb-[16px] text-[14px] leading-[22px]">
            {{ t('common.disclaimerSbcConnect') }}
          </div>

          <hr>
        </div>

        <UFormGroup name="jobTitle" class="mobile:mb-[16px]" help="Enter your current job title or position">
          <UInput v-model="temp" aria-label="extension" placeholder="Position/Title" />
        </UFormGroup>

        <div class="flex flex-row justify-between w-full mb-[40px] mobile:flex-col mobile:mb-[16px] space-x-2">
          <UFormGroup name="phoneNumber" class="flex-grow mobile:mb-[16px]">
            <UInput v-model="temp" type="tel" aria-label="phone number" placeholder="Phone Number" />
          </UFormGroup>
          <UFormGroup name="extension" class="flex-grow">
            <UInput
              v-model="temp"
              :placeholder="t('createAccount.contactForm.extension')"
              aria-label="extension"
            />
          </UFormGroup>
        </div>

        <UInput v-model="temp" :placeholder="t('createAccount.contactForm.faxNumber')" aria-label="extension" />
        <UInput v-model="temp" :placeholder="t('createAccount.contactForm.emailAddress')" aria-label="extension" />
        <BcrosAlertsMessage v-if="props.showAlertMsg" :flavour="AlertsFlavourE.INFO">
          {{ t('platformApplication.step1.alertMessage') }}
        </BcrosAlertsMessage>
      </div>
    </div>
  </FormCard>
</template>

<style scoped></style>
