/**
 * MEDICAL INTEGRATION UTILITIES
 * Scaling Through Integration: Medical Records, Devices, Services
 * 
 * Philosophy:
 * - Everyone is different, but everyone has medical records
 * - Collate existing programs, meds, medical services
 * - Philosophy is universal, data is diverse
 */

import {
  MedicalRecordIntegration,
  FHIRIntegration,
  HL7Integration,
  EMRIntegration,
  DeviceIntegration,
  AppIntegration
} from '../types/medicalIntegration';

/**
 * Create FHIR Integration
 * Fast Healthcare Interoperability Resources
 */
export function createFHIRIntegration(
  fhirVersion: string = 'R4',
  fhirEndpoint: string = '',
  fhirResources: string[] = ['Patient', 'Condition', 'Medication', 'Observation']
): FHIRIntegration {
  return {
    fhirVersion,
    fhirEndpoint,
    fhirResources
  };
}

/**
 * Create HL7 Integration
 * Healthcare data exchange standards
 */
export function createHL7Integration(
  hl7Version: string = 'v2',
  hl7Endpoint: string = '',
  hl7MessageTypes: string[] = ['ADT', 'ORU', 'OMG']
): HL7Integration {
  return {
    hl7Version,
    hl7Endpoint,
    hl7MessageTypes
  };
}

/**
 * Create EMR Integration
 * Electronic Medical Records
 */
export function createEMRIntegration(
  emrSystem: string = 'Epic',
  emrEndpoint: string = '',
  emrAuth: 'OAuth2' | 'SMART' | 'Basic' = 'OAuth2'
): EMRIntegration {
  return {
    emrSystem,
    emrEndpoint,
    emrAuth
  };
}

/**
 * Create Device Integration
 * Medical devices and wearables
 */
export function createDeviceIntegration(
  cgm: string[] = ['Dexcom', 'FreeStyle', 'Medtronic'],
  pump: string[] = ['Tandem', 'Omnipod', 'Medtronic'],
  wearable: string[] = ['Apple Watch', 'Fitbit', 'Garmin']
): DeviceIntegration {
  return {
    cgm,
    pump,
    wearable
  };
}

/**
 * Create App Integration
 * Health apps and platforms
 */
export function createAppIntegration(
  health: string[] = ['Apple Health', 'Google Fit'],
  nutrition: string[] = ['MyFitnessPal', 'Cronometer'],
  exercise: string[] = ['Strava', 'Nike Run Club']
): AppIntegration {
  return {
    health,
    nutrition,
    exercise
  };
}

/**
 * Create Medical Record Integration
 * Complete medical integration system
 */
export function createMedicalRecordIntegration(
  fhirVersion: string = 'R4',
  hl7Version: string = 'v2',
  emrSystem: string = 'Epic'
): MedicalRecordIntegration {
  const fhir = createFHIRIntegration(fhirVersion);
  const hl7 = createHL7Integration(hl7Version);
  const emr = createEMRIntegration(emrSystem);
  const devices = createDeviceIntegration();
  const apps = createAppIntegration();
  
  return {
    fhir,
    hl7,
    emr,
    devices,
    apps,
    timestamp: new Date().toISOString()
  };
}

/**
 * Check Medical Integration Status
 * Verify medical integration is active
 */
export function checkMedicalIntegrationStatus(integration: MedicalRecordIntegration): {
  fhirReady: boolean;
  hl7Ready: boolean;
  emrReady: boolean;
  devicesReady: boolean;
  appsReady: boolean;
  status: 'full' | 'partial' | 'none';
} {
  const fhirReady = integration.fhir.fhirEndpoint !== '';
  const hl7Ready = integration.hl7.hl7Endpoint !== '';
  const emrReady = integration.emr.emrEndpoint !== '';
  const devicesReady = integration.devices.cgm.length > 0 || 
                       integration.devices.pump.length > 0 || 
                       integration.devices.wearable.length > 0;
  const appsReady = integration.apps.health.length > 0 || 
                    integration.apps.nutrition.length > 0 || 
                    integration.apps.exercise.length > 0;
  
  const status = fhirReady && hl7Ready && emrReady && devicesReady && appsReady
    ? 'full'
    : (fhirReady || hl7Ready || emrReady || devicesReady || appsReady)
    ? 'partial'
    : 'none';
  
  return {
    fhirReady,
    hl7Ready,
    emrReady,
    devicesReady,
    appsReady,
    status
  };
}
