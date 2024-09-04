import { PlatformApplicationI } from '~/interfaces/platform-application-i'

export const usePlatformStore = defineStore('platformStore', () => {
  const state: PlatformApplicationI = reactive({ ...platformState })

  return { state }
})
